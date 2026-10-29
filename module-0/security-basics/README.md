# Security basics

About an hour. No code in this part, just the ideas you'll lean on in every project. Grab a notebook for the checks.

---

## Part 1: How attacks actually happen (~30 min)

Films make hacking look like someone typing very fast in a dark room while green text scrolls past. Real attacks are usually a lot more boring, and that's exactly why they work.

**Cybersecurity** is about keeping computers, accounts and information safe from people who shouldn't be messing with them. Defenders usually think about protecting three things:

- **Keeping secrets secret.** Your messages, marks, bank details. Only the right people should see them. (The textbook word is *confidentiality*.)
- **Making sure nothing gets changed behind your back.** Nobody should be able to quietly edit your exam result or the amount on a payment. (*Integrity*.)
- **Keeping things working when you need them.** A school website that's been knocked offline on results day is a security problem too. (*Availability*.)

So how do attackers get in? Mostly through a handful of tricks that have worked for years:

**Phishing.** A fake message, usually an email or text, pretending to be someone you trust: your bank, your school, a delivery company. It wants you to click a link, type a password, or open a file. Over and over, it's the most common way attacks start. You'll build a phishing link spotter in Project 2.

**Weak or reused passwords.** If your password is `cricket123`, someone can just guess it. If you use the same password everywhere, one leak from some random website hands the attacker your email, your games and your social media. That's what Project 1 is about.

**Guessing over and over.** Attackers use programs that try thousands of passwords against one account, or one common password against thousands of accounts. This is called a **brute-force attack**. It leaves a trail in the logs, which is what you'll hunt for in Project 3.

**Out-of-date software.** Apps and systems have bugs, and some bugs let attackers in. Companies release fixes (called **patches**), but only if people actually install the updates. That "update available" pop-up you keep ignoring? Often a security fix.

**Malware.** Short for "malicious software": programs built to do harm, like stealing passwords or locking your files until you pay up (that one's called **ransomware**). It usually sneaks in through a phishing email or a dodgy download.

**Tricking people.** Sometimes there's no technology involved at all. Someone rings the school office pretending to be from IT and asks for a password. Using lies and pressure to get people to hand things over is called **social engineering**, and phishing is one type of it.

Notice the pattern? Most of these go after people, not machines. A locked door doesn't help much if someone can talk you into opening it.

### Quick check: spot the clues

Here's a made-up email. Read it carefully, then write down at least **five** things that make it look like phishing.

```
From:    Nimbus Bank Security <alerts@nimbusbank-secure-mail.xyz>
Subject: URGENT!! Your account will be closed in 24 hours

Dear Customer,

We have detected unusual activity on you're account. To avoid
permanent suspension you must verify your details immediately.

Click here to verify: http://nimbusbank.com.account-verify.xyz/login

If you do not respond within 24 hours your account and all money
in it will be lost.

Nimbus Bank Security Team
```

(Nimbus Bank isn't real. Neither is anything else in this kit.)

---

## Part 2: How defenders think (~30 min)

If attackers only need one way in, defenders have to think about all of them. Nobody can do that perfectly, so good defenders lean on a few habits.

**Know what you're protecting.** You can't defend everything equally. A school's exam results and staff passwords matter more than the canteen menu. Working out what matters most, and who might want it, is step one.

**Build layers.** Don't rely on one lock. If a password gets guessed, a second step (like a code sent to a phone, called **two-step login** or **2FA**) can still stop the attacker. If someone clicks a phishing link, a filter might block the fake site. Each layer catches some of what the last one missed. People call this **defence in depth**.

**Give people only what they need.** A student account shouldn't be able to change marks. A bot that answers library questions shouldn't know the admin code. The less access each person or program has, the less damage they can do if something goes wrong. This is the **principle of least privilege**.

**Keep records, and actually read them.** Computers can write down everything that happens: every login, every file opened, every error. These records are called **logs**. When something odd happens, logs are how you work out what, when and who. Most security teams have tools that watch logs automatically and raise an **alert** when something looks off.

**Assume something will get through.** Good teams don't just try to stop attacks. They plan for how they'll spot one fast and clean it up. The quicker you notice, the less harm gets done.

**Stay on the right side of the line.** Everything in this kit is a skill defenders use. The exact same skills, used on something you don't own or don't have permission to test, are a crime in most countries. Professional "ethical hackers" (also called **penetration testers**) always have written permission before they test anything. Get in that habit now.

### Where the jobs are

A quick map of where this can lead. You'll see these again at the end of each project.

| Job | What they do, in one line |
|---|---|
| SOC analyst | Watches alerts and logs, works out which ones are real attacks. (SOC = Security Operations Centre.) |
| Penetration tester | Gets paid to break in, with permission, so problems get fixed before real attackers find them. |
| IAM engineer | Decides who can log in to what, and how. (IAM = Identity and Access Management.) |
| Security engineer | Builds and sets up the layers: filters, firewalls, alerts. |
| AI security specialist | Tests and protects AI systems, like chatbots, from being tricked or misused. |
| Automation engineer | Writes scripts so computers handle the boring, repetitive work and people can focus on the hard calls. |

### Quick check

1. A hospital's systems get locked by ransomware, and doctors can't see patient records for two days. Which of the three things (secrets, no sneaky changes, keeping things working) got hit hardest?
2. Your friend's password got leaked, but the attacker still couldn't log in. What layer might have stopped them?
3. Why shouldn't every teacher's account be able to change every student's marks?
4. You notice 200 failed logins on one account in five minutes. Where would you have seen that, and what's probably going on?
5. A classmate says, "I found a gap in the school website, let's see what we can get into." What should you tell them?

Answers are in [ANSWERS.md](ANSWERS.md).
