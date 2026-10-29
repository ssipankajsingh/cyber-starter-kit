# Python starter

← [Kit home](../../)

This isn't a coding course. You're going to learn just enough Python to do three small jobs that real security people do every week:

1. Check whether a password is any good
2. Count failed logins and decide when to raise the alarm
3. Read a log file and pull out the bits that matter

That's it. Around 75 minutes. Everything else you need, you'll pick up in the projects.

---

## Before you start: get Python running (~15 min)

**Install Python.** Go to [python.org/downloads](https://www.python.org/downloads/) and grab the latest version.

- On Windows, when the installer opens, tick the box that says **"Add python.exe to PATH"** before you click Install. Easy to miss, and things get annoying later if you skip it.
- On a Mac, just run the installer.

**Open a terminal.** A terminal is a window where you type commands instead of clicking things.

- Windows: press the Start key, type `Terminal` (or `Command Prompt`), and open it.
- Mac: press Cmd + Space, type `Terminal`, press Enter.

**Check it worked.** Type this and press Enter:

```
python --version
```

You should see something like `Python 3.13.1`. If you get an error, try `py --version` on Windows or `python3 --version` on a Mac. Whichever one works is the word you'll use to run scripts from now on.

**Get the kit.** [Download the kit as a ZIP file](https://github.com/ssipankajsingh/cyber-starter-kit/archive/refs/heads/main.zip) and unzip it somewhere you'll find again, like your Desktop. You'll get a folder called `cyber-starter-kit-main` with everything inside.

**Move into this folder.** In the terminal, `cd` means "change directory", which is a fancy word for folder. Type `cd ` (with a space), drag the `python-starter` folder into the terminal window, and press Enter.

**Run something.** Try:

```
python lesson1_password_check.py
```

It'll crash. That's expected. You haven't filled in the blanks yet.

### How the blanks work

Wherever you see `____` (four underscores), something's missing. Open the file in your editor, replace each `____` with the right thing, save, and run it again.

If you see this:

```
NameError: name '____' is not defined
```

you missed a blank. Python tells you the line number, so look there.

Hints for each blank are below. Solutions are in [ANSWERS.md](ANSWERS.md), but give it a real go first.

---

## Lesson 1: Is this password long enough? (~20 min)

Open `lesson1_password_check.py`. Here are the new ideas you'll meet. Read them, then look for them in the code.

- **`print()`** shows something on the screen.
- **A variable** is a name that holds a value. `password = "abc"` means "from now on, `password` means `abc`".
- **`input()`** asks the person a question and waits for them to type an answer.
- **`len()`** counts how many characters are in some text. `len("cat")` is `3`.
- **`if` / `else`** lets your code make a choice. If something is true, do this. Otherwise, do that.
- **`>=`** means "greater than or equal to". **`==`** means "is exactly equal to". One `=` stores a value; two `==` compares values. Everyone mixes these up at first.

Notice the lines inside an `if` are pushed in by 4 spaces. That's not just neatness. Python uses the spaces to know which lines belong to the `if`.

**Your blanks:**

1. The built-in tool that counts characters. You just read about it.
2. The minimum length. Security folks today usually say 12.
3. The word `password`, inside quotes: `"password"`. Quotes tell Python "this is text, not a variable name".

**Run it.** If you type `sunflower`, you should see:

```
=== Password length check ===
Type a made-up password: sunflower
That password has 9 characters.
Too short. Try for at least 12 characters.
Done!
```

Now try `PASSWORD` and something long like `my-cat-hates-mondays`.

### Quick check

1. What does a variable do?
2. What would `len("cyber")` give you?
3. If `length` is 12, is `length >= 12` true or false?
4. Why does the code use `.lower()` before comparing with `"password"`?
5. **Try it:** add a check so any password of 20 characters or more also prints `That's a passphrase. Great choice.`

---

## Lesson 2: Counting failed logins (~25 min)

When someone types a wrong password once, it's probably a typo. When it happens again and again in a short time, it might be an attacker trying password after password, hoping one works. That's called a **brute-force attack** (guessing over and over until something works).

Spotting it starts with something simple: counting.

New ideas:

- **A list** holds several values in order, inside square brackets: `["ok", "fail", "ok"]`.
- **A `for` loop** does the same thing for every item in a list. `for result in attempts:` means "take each item from `attempts`, call it `result`, and run the indented lines".
- **A counter** is a variable that starts at 0 and goes up by 1 each time something happens.

**Your blanks:**

1. The text that marks a failed login, in quotes. Look at the list at the top.
2. How much to add to the counter each time.
3. The variable that holds our limit. It's set just above.

**Run it.** You should see:

```
=== Failed login counter ===
Total attempts: 8
Failed attempts: 5
ALERT: more than 3 failed logins. Someone might be guessing the password.
```

### Quick check

1. The first time through the loop, what's in `result`?
2. Why does `failed` start at 0 and not 1?
3. Change the list so there are only two `"fail"` entries. What prints now?
4. Lots of websites lock an account after a few wrong passwords. Why not lock it after just one?
5. **Try it:** add a second counter that counts the successful logins, and print it at the end.

---

## Lesson 3: Reading a log file (~30 min)

Nobody types login records into a list by hand. Computers write them into **log files**, a running diary of what happened, one line per event. Reading logs is a huge part of a security analyst's day.

Open `login_attempts.txt` in your editor first. Each line has three bits of information separated by commas: the time, the username, and whether it worked. (All made up, by the way.)

New ideas:

- **`open()`** opens a file so Python can read it.
- **`for line in log_file:`** loops through the file one line at a time. Same idea as looping through a list.
- **`.strip()`** removes the invisible "new line" character at the end of each line.
- **`.split(",")`** chops text into a list of pieces wherever it finds a comma. `"21:04,admin,FAIL".split(",")` gives you `["21:04", "admin", "FAIL"]`.
- **Indexes:** to grab one item from a list, use its position in square brackets. Python starts counting at **0**, so `parts[0]` is the first piece, `parts[1]` the second. This catches everyone out at least once.

**Your blanks:**

1. The character that separates the columns, in quotes.
2. The position of the third piece. Remember, counting starts at 0.
3. The variable holding the username for this line.

**Run it.** The end of your output should be:

```
Lines read: 18
Failed logins: 9
```

Scroll up through the failed logins. Notice anything about `admin` around 21:05?

### Quick check: one tiny exercise

Six failed logins in 15 seconds, on the account with the most power. That's not someone who forgot their password.

**Add code that counts failed logins for the `admin` account only.** If there are more than 3, print:

```
ALERT: admin had 7 failed logins. Possible brute-force attack.
```

Hint: you'll need a new counter, and an `if` that checks two things. You can check two things at once with `and`, like `if result == "FAIL" and user == "admin":`.

---

## You made it

You've just used variables, `if`, lists, loops, counters and files, which honestly covers most of what you need for the projects. Head to [Project 1](../../project-1-password-checker/) and build your first real tool.
