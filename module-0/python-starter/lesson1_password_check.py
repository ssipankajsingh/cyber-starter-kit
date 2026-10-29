# Lesson 1: Is this password long enough?
#
# Fill in each ____ (four underscores), save the file, then run it.
# The README tells you what goes in each blank.

print("=== Password length check ===")

# input() shows a message and waits for you to type something.
# Whatever you type gets stored in the variable called password.
# Don't type a password you actually use. Make one up.
password = input("Type a made-up password: ")

# BLANK 1: which built-in tool counts the characters in some text?
length = ____(password)

print("That password has", length, "characters.")

# BLANK 2: what's the shortest length we're happy with?
if length >= ____:
    print("Good length. Long passwords are much harder to guess.")
else:
    print("Too short. Try for at least 12 characters.")

# A long password is no use if it's the first one an attacker tries.
# .lower() turns everything into small letters, so "PASSWORD" and
# "Password" get caught too.
# BLANK 3: the word password, in quotes.
if password.lower() == ____:
    print("Warning: that's one of the most guessed passwords on the planet.")

print("Done!")
