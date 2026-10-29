# Answers: Python starter

← [Kit home](../../)

Tried it yourself first? Good. Here you go.

## Lesson 1

**Blanks:** `len`, `12`, `"password"`

**Quick check**

1. It gives a value a name so you can use it later.
2. `5`
3. True. `>=` includes the number itself.
4. So `Password`, `PASSWORD` and `PaSsWoRd` all get caught, not just `password`.
5. Add this before `print("Done!")`:

```python
if length >= 20:
    print("That's a passphrase. Great choice.")
```

## Lesson 2

**Blanks:** `"fail"`, `1`, `limit`

**Quick check**

1. `"ok"`, the first item in the list.
2. Before the loop runs, we haven't counted any failures yet.
3. `Looks normal.` Two isn't more than three.
4. Everyone makes typos. Locking after one mistake would lock out real people all day long and flood the help desk.
5. One way:

```python
succeeded = 0
for result in attempts:
    if result == "fail":
        failed = failed + 1
    if result == "ok":
        succeeded = succeeded + 1

print("Successful logins:", succeeded)
```

## Lesson 3

**Blanks:** `","`, `2`, `user`

**Tiny exercise.** Add `admin_failed = 0` near the top, next to the other counters. Inside the loop, after the `result = ...` line:

```python
        if result == "FAIL" and user == "admin":
            admin_failed = admin_failed + 1
```

And at the very end:

```python
if admin_failed > 3:
    print("ALERT: admin had", admin_failed, "failed logins. Possible brute-force attack.")
```
