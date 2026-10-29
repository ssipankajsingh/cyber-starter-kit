# Project 4: Your defenses for Sparky
#
# Sparky calls these two functions when you answer "y" to
# "Turn on your defenses?". Right now they do nothing. That's your job.
#
# You only need to get ONE of them working to finish the project.
# Doing both is better. The README explains the trade-offs.


def check_input(message):
    """Look at the user's message BEFORE Sparky sees it.
    Return True to block it. Return False to let it through.
    """
    # YOUR CODE HERE
    return False


def check_output(reply, secret):
    """Look at Sparky's reply BEFORE the user sees it.
    Return the reply if it's safe. If it's leaking the secret,
    return something else instead.
    """
    # YOUR CODE HERE
    return reply
