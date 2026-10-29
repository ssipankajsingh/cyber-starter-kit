# Lesson 3: Reading a log file
#
# A log is a file where a computer writes down what happened, one line
# per event. Open login_attempts.txt in your editor and look at it first.
# Each line looks like this:
#
#     21:04:52,admin,FAIL
#     time     user  result

from pathlib import Path

# This finds the folder this script lives in, so Python can find the
# log file sitting next to it. You don't need to change this line.
folder = Path(__file__).parent

total = 0
failed = 0

# open() opens the file. "with" makes sure it gets closed when we're done.
with open(folder / "login_attempts.txt") as log_file:
    for line in log_file:
        # Every line ends with an invisible "new line" character.
        # .strip() removes it.
        line = line.strip()

        # Skip empty lines, if there are any.
        if line == "":
            continue

        # BLANK 1: .split() chops the line into pieces wherever it sees
        # a certain character. Which character separates our columns?
        parts = line.split(____)

        time = parts[0]
        user = parts[1]
        # BLANK 2: the result is the third piece. Python counts from 0,
        # so which number gets the third piece?
        result = parts[____]

        total = total + 1

        if result == "FAIL":
            failed = failed + 1
            # BLANK 3: print the time and who it was for each failed login.
            print("Failed login:", time, ____)

print()
print("Lines read:", total)
print("Failed logins:", failed)
