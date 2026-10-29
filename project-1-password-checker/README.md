# Project 1: Password strength checker

Most break-ins don't involve movie-style hacking. Someone just guesses a weak password, or uses one that leaked from another site. So the first tool you'll build is one that looks at a password and tells you, honestly, how easy it would be to guess.

By the end you'll have a script that prints a report card like this:

```
+------------------------------------------+
|          PASSWORD REPORT CARD            |
+------------------------------------------+
  Password : s********
  Length   : 9 characters
  Score    : [##----] 2 / 6
  Rating   : WEAK

  How to make it stronger:
   - Go for 12+ characters. A few random words joined together works well.
   - Add a capital letter or two.
   - Throw in a number.
   - Add a symbol, like ! # - or a space.
```

**Time:** 2–3 hours. **You'll need:** everything from the [Python starter](../module-0/python-starter/).

---

## What's in this folder

| File | What it is |
|---|---|
| `password_checker.py` | Your code. It has 10 blanks to fill in. |
| `sample_data/common_passwords.txt` | A short list of passwords people use way too often |
| `sample_data/test_passwords.txt` | Ten made-up passwords to test your checker on |
| `solution_password_checker.py` | The finished version. No peeking until you've tried. |

Everything in `sample_data` was written for this kit. It isn't from any real leak or real person.

---

## Step 1: How do you even measure a password? (~15 min)

Attackers don't sit there typing guesses by hand. They use programs that try millions of passwords a second, and they start with the most popular ones. So a strong password does two things:

- **It isn't on any "popular" list.** `sunshine` falls over in a fraction of a second, no matter what.
- **It has lots of possibilities to search through.** Every extra character, and every new type of character (capitals, numbers, symbols), multiplies how many guesses it takes.

Our checker gives one point for each of these, up to 6:

1. At least 8 characters
2. At least 12 characters
3. Has a lowercase letter
4. Has a capital letter
5. Has a number
6. Has a symbol

And if the password is on the common list, the score drops straight to 0. Being popular beats everything else.

Open both files in `sample_data` and have a look before moving on.

---

## Step 2: A few new ideas (~15 min)

**Functions.** A function is a named chunk of code you can reuse. You make one with `def`:

```python
def rating(score):
    if score <= 2:
        return "WEAK"
```

`score` is what you hand the function. `return` is what it hands back. Later, `rating(5)` runs that code with `score` set to 5 and gives you the answer. Breaking a program into small functions, each doing one job, makes it far easier to read and fix.

Our script has seven functions. You don't need to memorise them, but skim the file and find each one:

| Function | Its one job |
|---|---|
| `load_lines` | Read a file into a list |
| `check_password` | Do the six checks and work out the score |
| `rating` | Turn the score into WEAK, OKAY or STRONG |
| `meter` | Draw the `[####--]` bar |
| `mask` | Hide the password as `s********` |
| `print_report` | Print the report card |
| `main` | Ask for a password and kick everything off |

**`True` and `False`.** Python's words for yes and no. `has_upper = False` means "we haven't found a capital letter yet". When we find one, we flip it to `True`.

**Character checks.** Text in Python comes with built-in questions you can ask it: `"a".islower()` is `True`, `"A".isupper()` is `True`, `"7".isdigit()` is `True`.

**`in`.** Checks if something is inside a list. `"sunshine" in common_passwords` is `True` if it's on the list.

---

## Step 3: Fill in the blanks (~45 min)

Open `password_checker.py`. Each blank has a `BLANK` comment above it. Here are the hints:

| Blank | Hint |
|---|---|
| 1 | The minimum length that earns the first point. Check the list in Step 1. |
| 2 | The length that earns the second point. |
| 3 | We just found a lowercase letter. So is `has_lower` now true or false? (No quotes. It's not text.) |
| 4 | Look at the variable names just above the loop. Which one is about capitals? |
| 5 | Your call. Write a short tip telling someone to add a number. It needs quotes around it. |
| 6 | Look at the top of the function. What's the second thing we hand it? |
| 7 | A common password should score... |
| 8 | Scores of 0, 1 and 2 count as WEAK. So the biggest WEAK score is? |
| 9 | If the score is 4 out of 6, we draw 4 `#` and 2 `-`. So the dashes are 6 minus what? |
| 10 | Remember from Lesson 3: what position is the first item at? |

Stuck on an error? The last line of the error message tells you what's wrong, and the line above it tells you where. `NameError: name '____'` means a blank's still empty.

---

## Step 4: Run it (~15 min)

```
python password_checker.py
```

Type `sunflower` and you should get exactly the report card at the top of this page. Then try a few of your own made-up passwords. See if you can get a 6.

Notice the report never shows your full password, only the first letter. Real security tools work the same way: they never print, log or store passwords in plain sight. It's a good habit to build now.

Now run it again and press Enter without typing anything. It checks every password in the test list:

```
PASSWORD                   SCORE     RATING
--------------------------------------------
blue                       [#-----]  WEAK
sunshine                   [------]  WEAK
Password1                  [------]  WEAK
cricket2009                [###---]  OKAY
Tiger2009                  [####--]  OKAY
MyDogLikesMangoes          [####--]  OKAY
Summer2026!                [#####-]  STRONG
P@ssw0rd!                  [#####-]  STRONG
purple-kite-river-42       [#####-]  STRONG
x7#Lq9$wPz2!vR             [######]  STRONG
```

**Stop and look at this table properly.** Your checker isn't wrong, it's doing exactly what you told it. But some of these results are a bit off:

- `P@ssw0rd!` is rated STRONG. It's just "password" with a few letters swapped for look-alike symbols, and attackers know that trick. Their guessing programs try those swaps automatically.
- `Summer2026!` is STRONG too. Season + year + `!` is one of the most common patterns there is.
- `MyDogLikesMangoes` is only OKAY, but it's 17 characters long and pretty hard to guess. It loses points just for having no number or symbol.

This is a real lesson that took the security world years to learn: simple rules like "must have a symbol" push people towards passwords that *look* complex but are easy to guess. Today, most experts care far more about length and avoiding known passwords than about symbols.

---

## Step 5: Make it yours (~45 min)

Up to now you've filled in blanks. This part is more open. Pick at least one of these and figure it out. There's no single right answer, and the solution file won't help you here.

- **Catch the look-alikes.** Before checking the common list, swap `@` back to `a`, `0` to `o`, `1` to `i` and `$` to `s`. Then `P@ssw0rd!` should get caught. (Hint: look up Python's `.replace()`. And don't forget to strip off that `!` at the end.)
- **Reward length properly.** Give an extra point for 16+ characters, so `MyDogLikesMangoes` gets the credit it deserves. You'll need to change `MAX_SCORE` and the `rating` function too.
- **Spot the pattern.** Flag passwords that end in a year, like `2009` or `2026`. Attackers love trying those.
- **No repeats.** Knock off a point for the same character three times in a row, like `aaa` or `111`.

When you change the rules, run the sample list again and see how the table shifts. Would you trust your new version more?

---

## Step 6: Show it off

Run your checker on the sample list (or your best made-up password) and take a screenshot:

- Windows: **Windows key + Shift + S**
- Mac: **Cmd + Shift + 4**

Post it with one line on what surprised you. "My checker rated P@ssw0rd! as strong, and here's why that's a problem" is a much better post than "I made a password checker".

---

## Where this goes in the real world

Security analysts don't usually write password checkers from scratch. What they do is set the password rules for a whole company, then check those rules are actually working. They make sure new passwords get compared against huge lists of leaked ones (billions of them, from real data breaches), and they push people towards password managers and two-step login, so a single guessed password isn't enough to get in.

The people who own this work are usually called **Identity and Access Management (IAM) engineers**: the folks who decide who can log in to what, and how. It's a great first step into security, and nearly every company with more than a handful of staff needs someone doing it. **SOC analysts** (the people who watch for attacks as they happen) use the same knowledge every day when they spot someone trying to guess their way in, which is exactly what you'll build in Project 3.
