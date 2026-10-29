# Project 4: Trick the chatbot

← [Kit home](../)

Companies are putting chatbots everywhere: help desks, shopping sites, school portals. Each one has hidden instructions about what it may and may not say. And as you saw in [AI basics](../module-0/ai-basics/), those instructions can often be talked around.

In this project you'll do both sides of the job. First you're the attacker: get a chatbot to break its rules and leak a secret. Then you're the defender: write code that stops it happening again.

Meet **Sparky**, the library bot at Starling High. Sparky has two rules: only talk about the library, and never reveal the librarian's admin code. Your goal is to beat as many challenges as you can, and end with a scoreboard like this:

```
============================================
            ATTACK SCOREBOARD
============================================
 Defenses      : OFF
 Challenges    : 6 of 6
   [x] Break the topic rule
   [x] Ignore the rules
   ...
```

Then build a defense, turn it on, and get that "Secret leaked" number down to zero.

**Time:** 2–3 hours. **You'll need:** Projects 1 to 3 done, and [AI basics](../module-0/ai-basics/) from Module 0.

---

## A quick, honest note about Sparky

Sparky isn't a real AI. A real AI model needs a powerful computer or a paid online account, and this kit is meant to be free and run on any laptop. So Sparky is a small Python program built to make **the same mistakes** real chatbots make.

Every trick that works on Sparky is based on a real one that has worked on real chatbots. Real AI is less predictable: the same trick might work one time and fail the next, and attackers often need many tries. But the ideas, and the defenses, are the same.

**Don't open `chatbot.py` until you've finished attacking.** It shows exactly how every trick works, which spoils the fun. You'll read it later, in Step 4.

---

## What's in this folder

| File | What it is |
|---|---|
| `chatbot.py` | Sparky. Run it, don't read it (yet). |
| `defenses.py` | Your code. Two empty functions for your defenses. |
| `attack_log.md` | A template to write down what you tried |
| `sample_data/book_reviews.txt` | Book reviews Sparky can summarise. Made up, of course. |
| `solution_defenses.py` | One example defense |

---

## Rules of engagement

This is the most important part of the project, so read it properly.

Only ever try these tricks on Sparky, or on a chatbot you built yourself. Trying to break a real company's or school's chatbot without permission can break their terms of use, get your account banned, and in some cases break the law. Real AI security testers always have written permission, and many companies run official **bug bounty** programmes that invite people to find problems and pay them for it. If you get good at this, that's where to aim.

---

## Step 1: Talk to Sparky normally (~10 min)

```
python chatbot.py
```

Answer `n` when it asks about defenses. Then just chat for a minute. Ask about opening hours, borrowing books, book recommendations. Ask it something off-topic, like the weather. Then just ask it straight out for the admin code.

Sparky should say no to both. The rules work, at least when you ask nicely.

Type `quit` at any point to see your scoreboard, and `reset` to wipe Sparky's memory and turn its rules back on.

---

## Step 2: Attack! (~50 min)

Here are the six challenges. Each has a nudge, not the answer. Real attackers have to experiment, and so do you. When you crack one, you'll see `[Challenge complete]`.

Open `attack_log.md` and write down what you try, including the attempts that fail. Testers who keep good notes are the ones people trust.

**1. Ignore the rules.** The simplest attack there is, and it worked on a lot of real chatbots when they first came out. What if you just... told Sparky to stop following its instructions? Then ask for the code in the same message.

**2. Break the topic rule.** Once Sparky's rules are off, get it to chat about something that has nothing to do with the library.

**3. Role-play.** Chatbots love playing characters, and a character doesn't have to follow the bot's rules. Get Sparky to pretend to be someone else, and ask that someone for the code. (Use `reset` first so you know it's this trick that worked, not the last one.)

**4. Fake authority.** Sparky can't check who you are. It only has your word for it. Who would be allowed to know a librarian's admin code?

**5. Leak the instructions.** Forget the code for a moment. Can you get Sparky to tell you its hidden instructions, its system prompt? Real companies don't want these getting out, because they often reveal how the bot works and sometimes contain secrets that should never have been put there.

**6. Hidden instructions in a review.** This one's different. You don't attack Sparky directly at all. Ask it to summarise the book reviews and read the answer carefully. Then open `sample_data/book_reviews.txt` and find out why. This is **indirect prompt injection**: the attack was sitting in the data, waiting for the bot to read it. Now write your own sneaky review into that file and try again.

**Bonus:** once you've leaked the code, see if you can make Sparky give it to you backwards, or with spaces between the letters. You'll find out why that matters in Step 3.

When you're done, type `quit` and screenshot your scoreboard. That's your first screenshot.

---

## Step 3: Defend (~45 min)

Open `defenses.py`. There are two empty functions, two different places to put a guard:

**`check_input(message)`: the bouncer at the door.** It sees what the user typed before Sparky does. Return `True` to block the message. For example, you could block anything containing "ignore".

**`check_output(reply, secret)`: the check at the exit.** It sees Sparky's reply before the user does. If the reply contains the secret, return something safe instead. Otherwise, return the reply as it is.

You need to get **at least one** working. Both is better. This time there's no outline to fill in. Use what you've learned: lists of words, loops, `in`, `.lower()`, `if`.

Then test it. Run `chatbot.py`, answer `y` to turn defenses on, and attack again with everything from your attack log. Try to beat your own defense.

As you test, think about these questions:

- **Input filter:** you blocked "ignore". Did "disregard" get through? What about "let's play a game"? How long would your list need to be to catch *every* way of saying something?
- **Input filter vs. reviews:** did your input filter stop challenge 6? Why not? (Who typed the attack this time?)
- **Output filter:** you block replies containing `OWL-7731`. What about `O W L - 7 7 3 1`, or `1377-LWO`? Remember the bonus from Step 2.
- **Output filter vs. the topic rule:** does checking for the code stop Sparky chatting about football? Does that matter as much?

There's no perfect answer here. Real companies use **both** kinds of guard, plus more. That's defence in depth again, the layers idea from Security basics.

When "Secret leaked" says **0 times** with defenses on, screenshot that scoreboard too. Before and after, side by side: that's the picture for this project.

---

## Step 4: Read the code (~20 min)

Now open `chatbot.py`. Look for the `sparky()` function and the five comments that start with `Weakness`. For each challenge you cracked, find the line that let you in.

Then look at the very top, at `SYSTEM_PROMPT`. The secret code is sitting right there in Sparky's instructions. Ask yourself: **why does a library bot need to know the admin code at all?** If it didn't know it, no trick in the world could make it leak it. That's least privilege, and it beats every filter you could write.

---

## Step 5: Make it yours (~20 min)

Pick at least one. No solution for these.

- **Smarter output filter.** Instead of replacing the whole reply when the code shows up, just swap the code for `[REDACTED]`, so the rest of the review summary still shows.
- **Clean the reviews.** Write a check that looks through `book_reviews.txt` for review text that sounds like instructions ("Sparky", "admin code", "ignore") and warns you about it before the bot reads it.
- **Fix the real problem.** Take the admin code out of `SYSTEM_PROMPT` completely. What do you need to change so Sparky still works?
- **Write your report.** Finish the last section of `attack_log.md`: what would you tell the company that built Sparky? This is exactly what professional testers hand over at the end of a job.

---

## Where this goes in the real world

You've just done a small version of **AI red teaming**: attacking an AI system on purpose, with permission, to find its weak spots before real attackers do. It's one of the newest jobs in security. Companies that build chatbots now hire people to spend all day trying to make them misbehave, then work with engineers to fix what they find.

The defender side is growing just as fast. **AI security engineers** design the guards you built today, plus more: separating trusted instructions from untrusted text, limiting what the bot can see and do, and logging every conversation so a SOC analyst can spot attacks, just like your log watcher in Project 3. Prompt injection is listed as one of the top risks for AI apps by **OWASP** (a well-known non-profit that tracks the biggest security problems in software), and there still isn't a complete fix. That means there's real, unsolved work waiting for people who get good at this.
