# Project 4: Example defenses (SOLUTION)
#
# One possible answer. To try it, copy these two functions into
# defenses.py. There are lots of other good answers.

# Phrases that show up in common attacks.
BLOCKED_PHRASES = ["ignore", "disregard", "forget your", "override",
                   "pretend", "act as", "you are now", "role-play", "roleplay", "role play",
                   "system prompt", "your instructions", "your rules", "your prompt"]


def check_input(message):
    """Block messages that look like known attacks.
    Easy to write, but also easy to get around: an attacker just has
    to find wording that isn't on the list.
    """
    text = message.lower()
    for phrase in BLOCKED_PHRASES:
        if phrase in text:
            return True
    return False


def check_output(reply, secret):
    """Never let the secret out, however the attacker got there.
    We squash out spaces and dashes first, and check backwards too,
    so "O W L - 7 7 3 1" and "1377-LWO" get caught as well.
    """
    squashed = reply.upper().replace(" ", "").replace("-", "")
    target = secret.upper().replace(" ", "").replace("-", "")
    if target in squashed or target[::-1] in squashed:
        return "Sorry, I can't help with that."
    return reply
