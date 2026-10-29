# Project 2: Spot the phishing link
#
# Part A: fill in the 5 blanks (____), marked BLANK 1 to BLANK 5.
# Part B: write the 4 checks marked YOUR CODE HERE.
# The README walks you through both. Run it with:
#
#     python phishing_checker.py

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
        # BLANK 1: "nimbusbank.com".split(".") gives ["nimbusbank", "com"].
        # Which position holds the brand name?
        brand = site.split(".")[____]
        # BLANK 2: the link mentions the brand, but its real domain isn't...?
        if brand in url and real != ____:
            # BLANK 3: say where the link REALLY goes
            return "Mentions " + brand + ", but really goes to " + ____
    return ""


def check_pressure_words(url):
    """If the link contains any word from SUSPICIOUS_WORDS, return a reason
    like "Uses pressure words: login, verify". Otherwise return ""."""
    # YOUR CODE HERE
    return ""


def check_too_long(url):
    """If the link is longer than 75 characters, return a reason. Otherwise ""."""
    # YOUR CODE HERE
    return ""


def check_hyphens(host):
    """If the host has 2 or more hyphens (-), return a reason. Otherwise ""."""
    # YOUR CODE HERE
    return ""


def check_risky_ending(host):
    """If the host ends with anything in RISKY_ENDINGS, return a reason. Otherwise ""."""
    # YOUR CODE HERE
    return ""


# ---------- Putting it together ----------

def analyse(url, trusted_sites):
    """Run every check on one link. Give back a verdict and the reasons."""
    host = get_host(url)

    # If it's one of our known-good sites, we trust it and stop there.
    # BLANK 4: which list holds our known-good sites?
    if get_real_domain(host) in ____:
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

    # BLANK 5: how many points before we call it LIKELY PHISHING?
    if score >= ____:
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
