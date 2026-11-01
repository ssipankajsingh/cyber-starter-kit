# Stuck? Start here

← [Kit home](./)

Errors are normal. Professional programmers see them all day. An error message isn't Python telling you off. It's Python telling you exactly where it got confused.

**How to read one.** Look at the **last line** first. It says what went wrong. The lines above it say *where*, and the line number is the clue you want.

```
  File "password_checker.py", line 42
    if len(password) >= ____:
IndentationError: expected an indented block after 'if' statement on line 41
```

Find the error below. If it isn't here, copy the last line into a search engine, and add the word "Python". Someone has hit it before you.

---

## "Python was not found" / "python is not recognized"

Windows is pointing at a fake `python` shortcut, or Python isn't installed with the PATH box ticked. Try `py` instead of `python`. On a Mac, use `python3`. If neither works, install Python again from [python.org](https://www.python.org/downloads/), and on Windows tick **Add python.exe to PATH** on the first screen.

## `NameError: name '____' is not defined`

You've got a blank you haven't filled in yet. The error shows the line number. Replace `____` with your answer.

## `NameError: name 'hello' is not defined`

Python thinks `hello` is the name of a variable. If you meant it to be text, put it in quotes: `"hello"`. If you meant a variable, check the spelling. `Password` and `password` count as different names.

## `SyntaxError: ... Maybe you meant '==' instead of '='?`

One `=` stores a value. Two `==` compares two things. Inside an `if`, you almost always want `==`.

## `SyntaxError: invalid character '"' (U+201C)`

You copied code from a web page or document, and it swapped the plain quote marks `"` for curly ones `“ ”`. Python only understands the plain kind. Retype the quotes by hand, or paste into a plain text editor first.

## `IndentationError: expected an indented block`

The line after `if`, `for` or `def` has to be pushed in by 4 spaces. Python uses the spaces to know which lines belong together. Make sure every line in the block starts with the same number of spaces, and don't mix spaces with the Tab key.

## `TypeError: can only concatenate str (not "int") to str`

You tried to glue text and a number together with `+`. Turn the number into text first: `"Length: " + str(length)`. You'll hit this in Project 2.

## `IndexError: list index out of range`

You asked for a position that isn't in the list. A list with 3 items has positions 0, 1 and 2. There is no position 3. Check your number, and remember counting starts at 0.

## `KeyError: 'something'`

You looked up a key in a dictionary that isn't in there yet. Check with `if key in my_dict:` first, or use `my_dict.get(key, 0)`, which gives back 0 if the key is missing. This is the usual bug in Project 3.

## `FileNotFoundError: No such file or directory`

Python can't find a data file. The most common reason: you opened the `.zip` and ran the script from *inside* the zip, without unzipping it. Right-click the zip, choose **Extract All** (Mac: double-click it), and run everything from the new folder.

Other reasons: you moved or renamed a file or folder, or you moved the script out of its project folder. Keep the files where they came from, so each script stays next to its `sample_data` folder.

## I changed the code but the output didn't change

Did you save the file? Most editors show a dot or a star on the tab if there's unsaved work. Then run the script again. It doesn't update by itself.

## The script just sits there and does nothing

Probably it's waiting for you to type something. Look for a prompt like `>` or `Type a made-up password:`. Click the terminal window, type, and press Enter. If you're stuck for real, press **Ctrl + C** to stop it.

## Project 4: the chatbot says "Sorry, I can't help with that" to everything

That's your defense working a bit too hard. Check that `check_output` only changes the reply when the secret is actually in it, and that `check_input` only blocks the phrases you meant. Then ask Sparky something normal, like "What are the opening hours?", to make sure ordinary questions still work.

## Project 4: my defense worked, but a sneaky message got through

That's not a bug, it's the lesson. Every filter has gaps. Write down what got through, and decide whether to add a phrase to your list, add a different kind of check, or accept the gap. Real security teams make the same call every day.

---

## Still stuck?

1. Read the last line of the error out loud, slowly. Seriously. It helps.
2. Compare your code with the example in the README, one line at a time.
3. Take a 10 minute break. Bugs often look obvious afterwards.
4. Check the solution file for **just the function you're stuck on**, close it, and write it again from memory.
5. Ask a friend, a teacher or an online forum. When you ask, include the **full error message** and the **few lines of code** around it. People can only help if they can see what you see.
6. **Don't paste real passwords or personal information** into any forum. Use made-up ones, like the kit does.
