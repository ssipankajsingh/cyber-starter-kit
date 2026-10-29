# Lesson 2: Counting failed logins
#
# Picture a website that writes down every login attempt on one account.
# Here's that account's record for one evening.
# "ok" means the login worked. "fail" means the password was wrong.

attempts = ["ok", "fail", "ok", "fail", "fail", "fail", "fail", "ok"]

print("=== Failed login counter ===")
print("Total attempts:", len(attempts))

# We start counting at zero.
failed = 0

# A for loop goes through the list one item at a time.
# Each time round, the current item is stored in result.
for result in attempts:
    # BLANK 1: which word marks a failed login? Keep the quotes.
    if result == ____:
        # BLANK 2: how much do we add to the count each time?
        failed = failed + ____

print("Failed attempts:", failed)

# Security teams pick a limit. Go over it, and someone gets an alert.
limit = 3

# BLANK 3: which variable holds our limit?
if failed > ____:
    print("ALERT: more than", limit, "failed logins. Someone might be guessing the password.")
else:
    print("Looks normal.")
