# Project 2: Spot the phishing link

← [Kit home](../)

Phishing is how most attacks begin: a message with a link that looks like it's from your bank or your school, but isn't. Security teams can't check every link by eye, so they use tools that look for the tell-tale signs automatically. You're going to build one.

Your script will read a list of 20 links and sort each one into **TRUSTED**, **LOOKS OK**, **SUSPICIOUS** or **LIKELY PHISHING**, with reasons, like this:

```
[LIKELY PHISHING] http://nimbusbank.com.secure-verify.xyz/login
      - Mentions nimbusbank, but really goes to secure-verify.xyz
      - Uses http, not https, so the connection isn't encrypted
      - Uses pressure words: login, verify, secure
      - Ends in .xyz, which is cheap and popular with scammers
```

It also saves the whole report to a file you can share.

**Time:** 2–3 hours. **You'll need:** [Project 1](../project-1-password-checker/) done.

---

## What's in this folder

| File | What it is |
|---|---|
| `phishing_checker.py` | Your code. 5 blanks, then 4 checks to write yourself. |
| `sample_data/links.txt` | 20 made-up links to check |
| `sample_data/trusted_sites.txt` | Sites we know are genuine |
| `solution_phishing_checker.py` | The finished version, for when you're properly stuck |

All the companies here (Nimbus Bank, Kettlecart, Pixelpost, Starling High) are invented for this kit. **Don't paste any of these links into a browser.** Your script never visits them. It only reads the text, which is exactly how you want to handle a suspicious link.

---

## Step 1: Learn to read a link like an attacker (~20 min)

This is the most useful thing in this whole project, and it doesn't need any code.

Take this link:

```
http://nimbusbank.com.secure-verify.xyz/login
```

Your eye goes to `nimbusbank.com` at the start, and you think "that's my bank". But that's not how website addresses work. The part that matters is the **host**: everything between `//` and the next `/`. And you read the host **from the right**:

```
nimbusbank.com.secure-verify.xyz
               └──────┬────────┘
             this is who owns it
```

The last two pieces, `secure-verify.xyz`, are the real website. Whoever owns `secure-verify.xyz` can put anything they like in front of it, including `nimbusbank.com.`. This is called a **lookalike domain**, and it fools a lot of people.

A few more signs that a link is dodgy:

- **`http://` instead of `https://`.** The `s` means the connection is encrypted (scrambled so nobody in between can read it). Any real login page uses `https`.
- **Numbers instead of a name**, like `http://192.0.2.15/...`. Real companies use names.
- **An `@` sign.** In `https://pixelpost.com@203.0.113.9/signin`, the browser ignores everything before the `@`. You'd actually land on `203.0.113.9`.
- **Pressure words** like *verify*, *urgent*, *prize*, *free*.
- **Really long links**, which push the real address off the edge of the screen.
- **Lots of hyphens**, like `free-prize-winner`.
- **Unusual endings** like `.xyz` or `.top`. They're cheap to buy, so scammers love them. Plenty of real sites use them too, so this is a small clue, not proof.

Open `sample_data/links.txt` now and, before writing any code, guess which links are dodgy. Write down your guesses. You'll compare them with your script at the end.

---

## Step 2: A few new ideas (~10 min)

**An empty string, `""`.** Text with nothing in it. Each check in our script returns a reason if it finds a problem, or `""` if it doesn't. Later, the script keeps every reason that isn't `""`.

**`urlparse`.** Python comes with tools for pulling links apart. `urlparse(url).hostname` gives you just the host. It's already used for you in `get_host()`.

**Negative indexes.** `parts[-1]` is the *last* item in a list, and `parts[-2:]` means "the last two items". Handy for reading from the right.

**Pairs.** In `analyse()` you'll see things like `(check_ip_address(host), 2)`. Brackets with a comma make a pair: a reason and how many points it's worth. Some clues are worse than others: pretending to be a brand is worth 3 points, a long link only 1.

**Saving to a file.** `open(REPORT_FILE, "w")` opens a file for **w**riting (it creates the file if it doesn't exist), and `f.write(...)` puts text in it. It's already written for you at the bottom of the script.

---

## Step 3, Part A: Fill in the blanks (~30 min)

Open `phishing_checker.py`. Skim the whole thing first. A lot is already written. Then fill in the five blanks:

| Blank | Hint |
|---|---|
| 1 | `"nimbusbank.com".split(".")` gives `["nimbusbank", "com"]`. Which position is the brand? |
| 2 | The link mentions the brand, but the real domain isn't the brand's actual site. Which variable holds the real site? |
| 3 | Where does the link *really* go? There's a variable for that at the top of the function. |
| 4 | Which list holds our known-good sites? Look at what `analyse` is given. |
| 5 | How many points before something counts as LIKELY PHISHING? A brand trick on its own (3 points) should be enough. |

Run it. You'll get a report, but it misses a lot. Look at this one:

```
[LOOKS OK] https://free-prize-winner.click/claim-now
```

Clearly not OK. That's because four of the checks are empty. Time to write them.

---

## Step 4, Part B: Write your own checks (~45 min)

Scroll to the four functions that say `# YOUR CODE HERE`. Each one has a note saying what it should do. This time there are no blanks. You write the lines yourself.

Each check follows the same shape as the ones already written above it, like `check_at_sign`. Look at those for the pattern: `if` something is wrong, `return` a reason; otherwise, `return ""`.

Hints, from easiest to hardest:

- **`check_too_long`:** `len()` works on links too. To glue a number into text, turn it into text first with `str()`: `"Very long link (" + str(len(url)) + " characters)"`.
- **`check_hyphens`:** text has a `.count()` tool. `"a-b-c".count("-")` is `2`.
- **`check_risky_ending`:** loop through `RISKY_ENDINGS`. Text has an `.endswith()` tool: `"site.xyz".endswith(".xyz")` is `True`.
- **`check_pressure_words`:** loop through `SUSPICIOUS_WORDS` and `append` each one you find in the link to a list. If the list isn't empty at the end, return a reason. To turn `["login", "verify"]` into `"login, verify"`, use `", ".join(found)`.

Run the script after each one and watch the report change. That's the best way to know it's working.

When all four are done, the summary at the bottom should say:

```
Checked 20 links:
  TRUSTED         5
  LOOKS OK        4
  SUSPICIOUS      3
  LIKELY PHISHING 8
```

Your reason wording can be different from the solution's. What matters is that the same links get flagged.

---

## Step 5: Where your tool gets it wrong (~15 min)

Compare the report with your guesses from Step 1. Then look closely at these two:

```
[SUSPICIOUS] https://riverside-public-library.org/account/renew
      - Uses pressure words: account
      - Lots of hyphens in the site name
```

That's probably just a library website. Your tool flagged something innocent. That's called a **false positive**.

```
[SUSPICIOUS] https://pixe1post.com/login/verify-your-account
      - Uses pressure words: login, verify, account
```

Look really closely. That's `pixe1post`, with the number **1** instead of the letter **l**. It's pretending to be Pixelpost, and your tool only rated it SUSPICIOUS because "pixelpost" doesn't appear in it. When a tool misses something bad, that's called a **false negative**.

Every real security tool has both problems. Make it stricter and you flag more innocent things (and people start ignoring the alerts). Make it looser and real attacks slip through. Getting that balance right is a big part of the job.

---

## Step 6: Make it yours (~30 min)

Pick at least one. No solution for these.

- **Catch lookalike letters.** Before the brand check, make a copy of the host with `1` swapped back to `l`, `0` to `o` and `4` to `a`. If the swapped version mentions a brand, flag it. `pixe1post` should become LIKELY PHISHING.
- **Fix the false positive.** Change the rules so the library link comes out as LOOKS OK, without letting any of the bad links through. Harder than it sounds.
- **Add your own links.** Make up five new tricky links in `links.txt`, with fictional company names, and see if your checker catches them. Swap lists with a friend and try to fool each other's checkers.
- **Check a link you type in.** Add an option to type in a single link and check just that one.

---

## Step 7: Show it off

Run the finished checker and screenshot the report, or open `phishing_report.txt` and share that. Good one-liner to go with it: "My script caught 8 phishing links, but one sneaky lookalike got past it. Here's how."

---

## Where this goes in the real world

Every day, security analysts look at emails people have reported as "maybe phishing" and decide what's real. The tools they use, like email filters and threat-checking services, run checks a lot like yours, plus a few extras: how old the website is (scam sites are often days old), whether it's on a known blocklist, and what's actually on the page.

When analysts find a real phishing link, they block it for the whole company, warn people, and check whether anyone already clicked. This sits squarely in the **SOC analyst** role, and in **email security** and **threat intelligence** (people who track what attackers are up to and share warnings). Writing small scripts to check hundreds of links at once is exactly the kind of **automation** that makes those teams faster.
