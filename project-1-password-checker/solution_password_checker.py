# Project 1: Password strength checker (SOLUTION)
#
# This is the finished version. Try password_checker.py yourself first!

from pathlib import Path

# Find the sample_data folder next to this script.
folder = Path(__file__).parent
COMMON_FILE = folder / "sample_data" / "common_passwords.txt"
TEST_FILE = folder / "sample_data" / "test_passwords.txt"

MAX_SCORE = 6


def load_lines(path):
    """Read a text file and give back a list of its lines, skipping blanks."""
    lines = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line != "":
                lines.append(line)
    return lines


def check_password(password, common_passwords):
    """Score a password from 0 to 6, and collect tips to make it better."""
    score = 0
    tips = []

    # Checks 1 and 2: length. Making it longer is the single biggest win.
    if len(password) >= 8:
        score = score + 1
    else:
        tips.append("Use at least 8 characters. 12 or more is better.")

    if len(password) >= 12:
        score = score + 1
    elif len(password) >= 8:
        tips.append("Go for 12+ characters. A few random words joined together works well.")

    # Checks 3 to 6: what kinds of characters are in there?
    has_lower = False
    has_upper = False
    has_digit = False
    has_symbol = False

    for ch in password:
        if ch.islower():
            has_lower = True
        elif ch.isupper():
            has_upper = True
        elif ch.isdigit():
            has_digit = True
        else:
            has_symbol = True

    if has_lower:
        score = score + 1
    else:
        tips.append("Add some lowercase letters.")

    if has_upper:
        score = score + 1
    else:
        tips.append("Add a capital letter or two.")

    if has_digit:
        score = score + 1
    else:
        tips.append("Throw in a number.")

    if has_symbol:
        score = score + 1
    else:
        tips.append("Add a symbol, like ! # - or a space.")

    # The deal-breaker. Attackers try common passwords first, so a
    # common password is weak no matter what else it has going for it.
    if password.lower() in common_passwords:
        score = 0
        tips = ["This is one of the most guessed passwords out there. Pick something else entirely."]

    return score, tips


def rating(score):
    """Turn a number score into a word."""
    if score <= 2:
        return "WEAK"
    elif score <= 4:
        return "OKAY"
    else:
        return "STRONG"


def meter(score):
    """Draw a little bar, like [####--] for a score of 4."""
    return "[" + "#" * score + "-" * (MAX_SCORE - score) + "]"


def mask(password):
    """Show only the first character. Real tools never print your password."""
    return password[0] + "*" * (len(password) - 1)


def print_report(password, score, tips):
    print()
    print("+------------------------------------------+")
    print("|          PASSWORD REPORT CARD            |")
    print("+------------------------------------------+")
    print("  Password :", mask(password))
    print("  Length   :", len(password), "characters")
    print("  Score    :", meter(score), score, "/", MAX_SCORE)
    print("  Rating   :", rating(score))
    print()
    if len(tips) == 0:
        print("  Nothing to fix. Nice work.")
    else:
        print("  How to make it stronger:")
        for tip in tips:
            print("   -", tip)
    print()


def check_sample_list(common_passwords):
    # These are made-up test passwords, so it's fine to show them in full.
    print()
    print("PASSWORD".ljust(26), "SCORE".ljust(9), "RATING")
    print("-" * 44)
    for password in load_lines(TEST_FILE):
        score, tips = check_password(password, common_passwords)
        print(password.ljust(26), meter(score).ljust(9), rating(score))
    print()


def main():
    common_passwords = load_lines(COMMON_FILE)

    print("=== Password Strength Checker ===")
    print("Type a made-up password (never a real one),")
    print("or just press Enter to test the sample list.")
    password = input("> ")

    if password == "":
        check_sample_list(common_passwords)
    else:
        score, tips = check_password(password, common_passwords)
        print_report(password, score, tips)


main()
