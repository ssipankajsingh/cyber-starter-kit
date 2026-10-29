# Project 3: Log watcher

← [Kit home](../)

Remember the `admin` account getting hammered in Module 0, Lesson 3? That was 18 lines, and you could spot the problem by eye. Real systems write thousands of lines an hour. Nobody reads them all. Instead, security teams write rules that read the logs for them and only shout when something looks wrong.

That's what you're building. Your script will read an evening's worth of login records, chart who failed the most, and raise alerts, including one for a login that really shouldn't have worked:

```
Failed logins by IP address
  203.0.113.45     ######################## 24
  192.0.2.77       ############ 12
  198.51.100.14    ###### 6
  ...

ALERTS
  [HIGH]   203.0.113.45 logged in as admin at 21:05:32 after 24 failures in a row
  ...
```

**Time:** 2–3 hours. **You'll need:** Projects 1 and 2 done.

This one is more open than the last two. There are no blanks. Instead there are four small functions to write, with notes on what each should do.

---

## What's in this folder

| File | What it is |
|---|---|
| `log_watcher.py` | Your code. 4 TODOs to finish. |
| `sample_data/auth.log` | One evening of login records for a made-up school system |
| `solution_log_watcher.py` | The finished version |

The log is entirely made up. The IP addresses come from ranges set aside for examples, so they don't belong to anyone.

---

## Step 1: Read the log yourself (~15 min)

Open `sample_data/auth.log` in your editor. Each line looks like this:

```
2026-03-14 21:04:12 FAIL user=admin ip=203.0.113.45
```

That's the date, the time, whether the login worked, which account someone tried, and the **IP address** it came from. An IP address is a number that identifies a device on a network, a bit like a postal address for computers. If lots of bad logins come from one IP, it's probably one person (or one program) doing it.

Scroll through for a couple of minutes. Can you spot anything odd? Search the file (Ctrl+F, or Cmd+F on a Mac) for `203.0.113.45`. Then try `192.0.2.77`. Write down what you think each one is up to.

---

## Step 2: Dictionaries (~15 min)

To count failures *per IP address*, you need something new. A list is fine for one counter, but here you need a separate counter for every address, and you don't know the addresses in advance.

A **dictionary** stores pairs: a **key** you look things up by, and a **value** that goes with it. Like a real dictionary, where you look up a word (the key) to find its meaning (the value).

```python
counts = {}                       # an empty dictionary
counts["203.0.113.45"] = 1        # add a key with a value
counts["203.0.113.45"] = counts["203.0.113.45"] + 1   # now it's 2
print(counts)                     # {'203.0.113.45': 2}
print("192.0.2.77" in counts)     # False, it's not in there yet
```

One catch: if you try to read a key that isn't there, Python crashes with a `KeyError`. So the first time you see an IP, you have to add it before you can add 1 to it. Two ways to deal with that:

```python
# Way 1: check first
if ip in counts:
    counts[ip] = counts[ip] + 1
else:
    counts[ip] = 1

# Way 2: .get() gives back 0 if the key isn't there yet
counts[ip] = counts.get(ip, 0) + 1
```

Both do the same thing. Use whichever makes more sense to you.

You'll also notice each log line becomes a dictionary in the script, so you can write `event["user"]` instead of trying to remember that the user is at position 3.

---

## Step 3: Finish the TODOs (~75 min)

Run `log_watcher.py` first, before changing anything. It works, but the report is empty. Run it again after each TODO and watch it fill in.

**TODO 1: Pull out the user and IP.** `parts[3]` is the text `"user=admin"`. You want just `admin`. You've used `.split()` before to chop text at commas. What could you chop this at? Once this works, nothing shows on screen yet, but the next TODOs depend on it.

**TODO 2: Count failures per IP.** Loop through `events`. Each one is a dictionary, so `event["result"]` tells you if it failed and `event["ip"]` tells you where from. Use the dictionary trick from Step 2. When this works, the "Failed logins" total at the top should say **58**, and you'll see a list of addresses with numbers.

**TODO 3: Draw the bars.** In Python, you can multiply text: `"ab" * 3` gives `"ababab"`. That's all you need.

**TODO 4: Catch the break-in.** This is the big one. Lots of failures is suspicious. Lots of failures *followed by a success* is worse, because it means the guessing worked.

Go through the events in order. For each IP, keep a count of how many times in a row it's failed. When an IP gets a success, check that count. If it was `LIMIT` or more, that's a break-in alert. Either way, reset that IP's count to 0, because the streak is over.

The notes in the code break this into steps. To add a pair to the list, it's `break_ins.append((event, in_a_row[ip]))`. Yes, two sets of brackets: the outer ones belong to `append`, the inner ones make the pair.

When it's all working, your ALERTS section should match this:

```
ALERTS
  [HIGH]   203.0.113.45 logged in as admin at 21:05:32 after 24 failures in a row
  [HIGH]   198.51.100.14 logged in as ben at 22:51:23 after 6 failures in a row
  [MEDIUM] 192.0.2.77 failed 12 times (no break-in seen)
  [MEDIUM] 198.51.100.21 failed 5 times (no break-in seen)
```

Stuck for more than 20 minutes on one TODO? Look at just that function in the solution file, then close it and write it yourself from memory.

---

## Step 4: Be the analyst (~20 min)

Your tool has done its job: four alerts out of 116 lines. Now comes the part a script can't do. For each alert, work out what's really going on. Look back at the log for each IP and decide: real attack, or not?

Some things to think about:

- **203.0.113.45:** 24 failures on `admin`, a few seconds apart, then a success. No human types that fast. What would you do first?
- **198.51.100.14:** That's `ben`, from the address he logs in from all evening. Six slow failures, then he gets in. Attacker, or someone who changed his password last week and keeps typing the old one?
- **192.0.2.77:** Never got in. But look at the usernames it tried. What's it doing? (Trying lots of common account names to see which exist is called **username guessing**. Trying one or two passwords on lots of accounts is called **password spraying**.)
- **198.51.100.21:** That's `zara`. Five failures, but when? Are they bunched together or spread over three hours?

If you decided Ben and Zara are probably fine, you've just found two **false positives**. That's normal. Analysts spend a lot of their day doing exactly this: checking alerts and closing the harmless ones.

---

## Step 5: Make it yours (~30 min)

Pick at least one. No solution for these.

- **Spot username guessing.** For each IP, collect the *different* usernames it tried (a list where you only `append` a name if it's not already `in` the list). Raise an alert for any IP that tried 5 or more different accounts.
- **Quiet the false positive.** Zara's failures are spread over hours. Change the MEDIUM alert so it only counts failures within the same 10 minutes. (Hint: the time is text like `"21:04:12"`. `int("21")` turns text into a number you can do maths with.)
- **Save the alerts.** Write the ALERTS section to `alerts.txt`, the way Project 2 saved its report.
- **Play with the limit.** Change `LIMIT` to 3, then 10. How many alerts do you get each time? Which number would you pick if you had to check every alert yourself, every night?

---

## Step 6: Show it off

Screenshot the full report: the bar chart plus alerts make a good picture. Even better, pair it with a sentence or two on what you decided in Step 4: "My log watcher flagged 4 alerts. One was a real break-in, two were people who forgot their passwords, and one was someone guessing account names."

---

## Where this goes in the real world

This is the bread and butter of a **SOC analyst**. Companies feed all their logs (logins, network traffic, file access, from thousands of computers) into a big system called a **SIEM** (Security Information and Event Management, basically a giant log search engine with alert rules). Detection rules in a SIEM work just like yours: "if one address fails more than N times then succeeds, raise a HIGH alert."

Analysts then do what you did in Step 4: investigate each alert, decide if it's real, and respond. That might mean locking an account, blocking an IP address, or calling someone to check it was really them. People who write and tune the rules are often called **detection engineers**, and making those rules catch more real attacks with fewer false alarms is a skill companies pay well for. Much of it comes down to the same Python you've just written.
