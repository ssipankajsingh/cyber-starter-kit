# Project 3: Log watcher (SOLUTION)
#
# This is the finished version. Try log_watcher.py yourself first!

from pathlib import Path

folder = Path(__file__).parent
LOG_FILE = folder / "sample_data" / "auth.log"

# How many failures from one address before we raise an alert.
LIMIT = 5


def parse_line(line):
    """Turn one log line into a dictionary.
    2026-03-14 21:04:12 FAIL user=admin ip=203.0.113.45
    -> {"date": "2026-03-14", "time": "21:04:12", "result": "FAIL",
        "user": "admin", "ip": "203.0.113.45"}
    """
    parts = line.split()
    event = {}
    event["date"] = parts[0]
    event["time"] = parts[1]
    event["result"] = parts[2]
    event["user"] = parts[3].split("=")[1]
    event["ip"] = parts[4].split("=")[1]
    return event


def count_failures_by_ip(events):
    """Count how many FAIL events came from each IP address.
    Gives back a dictionary like {"203.0.113.45": 24, "198.51.100.14": 7}
    """
    counts = {}
    for event in events:
        if event["result"] == "FAIL":
            ip = event["ip"]
            if ip in counts:
                counts[ip] = counts[ip] + 1
            else:
                counts[ip] = 1
    return counts


def find_break_ins(events):
    """Find successful logins that came straight after LIMIT or more
    failures in a row from the same IP address.
    Gives back a list of (event, failures_in_a_row) pairs.
    """
    in_a_row = {}
    break_ins = []
    for event in events:
        ip = event["ip"]
        if event["result"] == "FAIL":
            in_a_row[ip] = in_a_row.get(ip, 0) + 1
        elif event["result"] == "SUCCESS":
            if in_a_row.get(ip, 0) >= LIMIT:
                break_ins.append((event, in_a_row[ip]))
            in_a_row[ip] = 0
    return break_ins


def draw_bar(count):
    """A bar of # signs, one per failure."""
    return "#" * count


def main():
    events = []
    with open(LOG_FILE) as f:
        for line in f:
            line = line.strip()
            if line != "":
                events.append(parse_line(line))

    counts = count_failures_by_ip(events)
    break_ins = find_break_ins(events)

    total_failed = 0
    for ip in counts:
        total_failed = total_failed + counts[ip]

    print("=" * 50)
    print("               LOG WATCHER REPORT")
    print("=" * 50)
    print("Lines read     :", len(events))
    print("Failed logins  :", total_failed)
    print("Alert limit    :", LIMIT, "failures from one address")
    print()

    print("Failed logins by IP address")
    if len(counts) == 0:
        print("  (nothing counted yet)")
    # Sort so the address with the most failures comes first.
    ranked = sorted(counts, key=counts.get, reverse=True)
    for ip in ranked:
        print("  " + ip.ljust(16), draw_bar(counts[ip]), counts[ip])
    print()

    print("ALERTS")
    alerted = []
    for event, failures in break_ins:
        print("  [HIGH]   " + event["ip"] + " logged in as " + event["user"]
              + " at " + event["time"] + " after " + str(failures) + " failures in a row")
        alerted.append(event["ip"])
    for ip in ranked:
        if counts[ip] >= LIMIT and ip not in alerted:
            print("  [MEDIUM] " + ip + " failed " + str(counts[ip]) + " times (no break-in seen)")
            alerted.append(ip)
    if len(alerted) == 0:
        print("  No alerts.")


main()
