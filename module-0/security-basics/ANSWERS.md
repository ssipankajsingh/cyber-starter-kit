# Answers: Security basics

## Part 1: Spot the clues

Any five of these (there are more than five):

- **The sender's address is wrong.** It's from `nimbusbank-secure-mail.xyz`, not the bank's own website.
- **The link goes somewhere else.** Read the address from the end backwards: the real site is `account-verify.xyz`. The `nimbusbank.com` at the start is just decoration.
- **It uses `http`, not `https`.** A real bank login page would always be `https`.
- **Panic and a deadline.** "URGENT!!", "24 hours", "all money will be lost". Pressure is there to stop you thinking.
- **"Dear Customer".** Your real bank knows your name.
- **Spelling and grammar slips.** "you're account" should be "your account".
- **It asks you to "verify your details" through a link.** Real banks tell you to log in through their app or by typing their address yourself.

The golden rule: if a message makes you panic, slow down. Go to the website yourself instead of clicking the link.

## Part 2

1. **Keeping things working** (availability). Nothing was necessarily stolen or changed, but nobody could use the records when they needed them. Many ransomware gangs do steal data too, so secrets can get hit as well.
2. **Two-step login (2FA).** The attacker had the password, but not the code sent to the friend's phone.
3. **Least privilege.** If one of those accounts got hacked or a teacher made a mistake, the damage would spread to everyone. Teachers should only be able to change marks for their own classes.
4. **In the logs**, probably through an alert. It looks like a **brute-force attack**: someone running a program that guesses password after password.
5. Don't. Poking around a system you don't have permission to test is illegal, even if you mean well. If you think you've found a real problem, tell a teacher or the school's IT team and let them handle it. That's exactly what a professional would do.
