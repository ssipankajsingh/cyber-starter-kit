# Project 2: Spot the phishing link (SOLUTION)
#
# This is the finished version. Try phishing_checker.py yourself first!

from pathlib import Path
from urllib.parse import urlparse

folder = Path(__file__).parent
LINKS_FILE = folder / "sample_data" / "links.txt"
TRUSTED_FILE = folder / "sample_data" / "trusted_sites.txt"
REPORT_FILE = folder / "phishing_report.txt"

SUSPICIOUS_WORDS = ["login", "verify", "secure", "account", "update", "password", "prize", "free", "urgent"]
RISKY_ENDINGS = [".xyz", ".top", ".click", ".zip", ".info"]


def load_lines(path):
    """Read a text file and give back a list of its lines, skipping blanks."""
    lines = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line != "":
                lines.append(line)
    return lines


def get_host(url):
    """Pull out the website part of a link: https://www.site.com/page -> www.site.com"""
    host = urlparse(url).hostname
    if host is None:
        return ""
    return host


def is_ip_address(host):
    """True if the host is just numbers and dots, like 192.0.2.15"""
    return host.replace(".", "").isdigit()


def get_real_domain(host):
    """The real owner of a site is the LAST two pieces of the host.
    www.nimbusbank.com              -> nimbusbank.com
    nimbusbank.com.secure-login.xyz -> secure-login.xyz
    """
    if is_ip_address(host):
        return host
    parts = host.split(".")
    return ".".join(parts[-2:])


# ---------- The checks ----------
# Each check looks at one thing. It returns a reason (some text) if the
# link looks dodgy, or an empty string "" if it's fine.

def check_no_https(url):
    if url.startswith("http://"):
        return "Uses http, not https, so the connection isn't encrypted"
    return ""


def check_ip_address(host):
    if is_ip_address(host):
        return "Uses a number address instead of a website name"
    return ""


def check_at_sign(url):
    if "@" in url:
        return "Has an @ sign, which can hide where the link really goes"
    return ""


def check_brand_trick(url, host, trusted_sites):
    real = get_real_domain(host)
    for site in trusted_sites:
        brand = site.split(".")[0]
        if brand in url and real != site:
            return "Mentions " + brand + ", but really goes to " + real
    return ""


def check_pressure_words(url):
    found = []
    for word in SUSPICIOUS_WORDS:
        if word in url.lower():
            found.append(word)
    if len(found) > 0:
        return "Uses pressure words: " + ", ".join(found)
    return ""


def check_too_long(url):
    if len(url) > 75:
        return "Very long link (" + str(len(url)) + " characters), which can hide the real address"
    return ""


def check_hyphens(host):
    if host.count("-") >= 2:
        return "Lots of hyphens in the site name"
    return ""


def check_risky_ending(host):
    for ending in RISKY_ENDINGS:
        if host.endswith(ending):
            return "Ends in " + ending + ", which is cheap and popular with scammers"
    return ""


# ---------- Putting it together ----------

def analyse(url, trusted_sites):
    """Run every check on one link. Give back a verdict and the reasons."""
    host = get_host(url)

    # If it's one of our known-good sites, we trust it and stop there.
    if get_real_domain(host) in trusted_sites:
        return "TRUSTED", []

    # Each pair is (reason, points). Some clues are much worse than others.
    checks = [
        (check_brand_trick(url, host, trusted_sites), 3),
        (check_ip_address(host), 2),
        (check_at_sign(url), 2),
        (check_no_https(url), 1),
        (check_pressure_words(url), 1),
        (check_too_long(url), 1),
        (check_hyphens(host), 1),
        (check_risky_ending(host), 1),
    ]

    reasons = []
    score = 0
    for reason, points in checks:
        if reason != "":
            reasons.append(reason)
            score = score + points

    if score >= 3:
        return "LIKELY PHISHING", reasons
    elif score >= 1:
        return "SUSPICIOUS", reasons
    else:
        return "LOOKS OK", reasons


def main():
    links = load_lines(LINKS_FILE)
    trusted_sites = load_lines(TRUSTED_FILE)

    counts = {"TRUSTED": 0, "LOOKS OK": 0, "SUSPICIOUS": 0, "LIKELY PHISHING": 0}
    report = []
    report.append("=== PHISHING LINK REPORT ===")
    report.append("")

    for url in links:
        verdict, reasons = analyse(url, trusted_sites)
        counts[verdict] = counts[verdict] + 1
        report.append("[" + verdict + "] " + url)
        for reason in reasons:
            report.append("      - " + reason)

    report.append("")
    report.append("Checked " + str(len(links)) + " links:")
    for verdict in counts:
        report.append("  " + verdict.ljust(16) + str(counts[verdict]))

    # Show the report on screen, and save a copy to a file.
    for line in report:
        print(line)
    with open(REPORT_FILE, "w") as f:
        for line in report:
            f.write(line + "\n")
    print()
    print("Report saved to", REPORT_FILE.name)


main()
