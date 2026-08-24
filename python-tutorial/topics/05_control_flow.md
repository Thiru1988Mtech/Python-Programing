# 05 — Control Flow (from absolute zero)

## 1. Real-life analogy

**Conditionals (`if`)** are like a bouncer at a club: *"IF you're 18+, let
them in. ELSE, don't."* Only one path gets taken.

**Loops** are like a washing machine cycle: *"REPEAT rinse-and-spin WHILE
there's still soap in the water."* The same action happens over and over
until a condition changes.

## 2. `if` statements — one path is chosen

```python
marks = 72

if marks >= 90:
    print("Grade A")
```
Read as: *"IF marks is 90 or more, THEN print Grade A."* If the condition
is `False`, nothing happens — the line inside is simply skipped.

**Indentation matters enormously in Python.** The indented lines (usually
4 spaces) BELONG to the `if` above them. This is how Python knows what's
"inside" the condition.

```python
if marks >= 90:
    print("Grade A")     # <- this line is INSIDE the if (indented)
print("Done checking")   # <- this line is OUTSIDE the if (not indented) - always runs
```

## 3. `if / elif / else` — multiple paths, only ONE is chosen

```python
marks = 72

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Grade F")
```

**Trace it step by step with `marks = 72`:**
1. Check `marks >= 90` → `72 >= 90` → `False` → skip, move to next check
2. Check `marks >= 75` → `72 >= 75` → `False` → skip, move to next check
3. Check `marks >= 60` → `72 >= 60` → `True` → print "Grade C" and **STOP
   checking the rest** (even though the next ones might also be true)
4. Output: `Grade C`

> 🧠 Order matters! If you wrote `marks >= 60` FIRST, then even a 95 would
> incorrectly print "Grade C" because it stops at the first True match.
> Always order your checks from most-strict to least-strict.

## 4. Nested `if` — a condition inside another condition

```python
age = 20
has_ticket = True

if age >= 18:
    if has_ticket:
        print("Welcome in!")
    else:
        print("You need a ticket.")
else:
    print("Sorry, you must be 18+.")
```
Read as: *"FIRST check age. IF that passes, THEN check the ticket too."*
This is the same logic as `age >= 18 and has_ticket`, just written as two
separate steps instead of one combined condition — both are valid, use
whichever is clearer to you.

## 5. `for` loops — repeat for each item in a collection

```python
fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print("I like", fruit)
```
Read as: *"For EACH fruit found in the fruits list, one at a time, do the
indented action."*

**Trace it:** Python takes fruit #1 ("apple"), runs the indented line,
then goes BACK to get fruit #2 ("banana"), runs the line again, then fruit
#3 ("mango"), runs it again, then the list is empty — loop ends
automatically.

### `range()` — generating numbers to loop through
```python
for i in range(5):        # generates 0, 1, 2, 3, 4 (5 numbers, starting at 0)
    print("Count:", i)

for i in range(1, 6):     # generates 1, 2, 3, 4, 5 (start, stop)
    print(i)

for i in range(0, 10, 2): # generates 0, 2, 4, 6, 8 (start, stop, step)
    print(i)
```

## 6. `while` loops — repeat WHILE a condition stays true

```python
count = 0

while count < 3:
    print("Running... count =", count)
    count += 1     # 🚨 CRITICAL: without this line, count never changes,
                   # the condition NEVER becomes False, and this loops FOREVER
```

**Trace it:**
1. `count = 0`. Check `0 < 3` → True → print, then `count` becomes 1
2. Check `1 < 3` → True → print, then `count` becomes 2
3. Check `2 < 3` → True → print, then `count` becomes 3
4. Check `3 < 3` → False → loop stops

> 🧠 The #1 beginner bug: an infinite loop, caused by forgetting to update
> the variable being checked. If your program seems "frozen" and never
> finishes, this is almost always why. Press Ctrl+C to force-stop it.

## 7. `break` and `continue` — controlling a loop from inside

```python
# break -> exits the loop COMPLETELY, right now
for number in range(10):
    if number == 5:
        break
    print(number)
# Output: 0 1 2 3 4  (stops entirely once it hits 5)

# continue -> skips just THIS ONE round, but keeps looping
for number in range(5):
    if number == 2:
        continue
    print(number)
# Output: 0 1 3 4  (skips only the number 2, keeps going after)
```

## 8. Full worked example — combining everything

```python
# A simple number guessing checker
secret_number = 7
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    guess = int(input("Guess the number (1-10): "))
    attempts += 1

    if guess == secret_number:
        print("🎉 Correct! You win!")
        break
    elif guess < secret_number:
        print("Too low, try again.")
    else:
        print("Too high, try again.")

    if attempts == max_attempts:
        print(f"Game over! The number was {secret_number}.")
```

## 9. Common mistakes

```python
if marks >= 90
    print("A")   # ❌ SyntaxError: missing colon ":" after the condition
```

```python
count = 0
while count < 5:
    print(count)   # ❌ forgot to increase count -> INFINITE LOOP
```

## 10. Practice

1. Write `if/elif/else` for a temperature: `< 15` = "Cold", `15-30` =
   "Nice", `> 30` = "Hot". Test with 3 different values.
2. Use a `for` loop to print all numbers from 1 to 20 that are even
   (hint: use `%`).
3. Use a `while` loop that keeps asking "Enter password:" until the user
   types the correct password `"python123"`.
4. Loop through `[3, 7, 2, 9, 4, 15]` and print only numbers greater than
   5, using `continue` to skip the rest.

---
⬅ [Previous: Data Structures](04_data_structures.md) | ➡ [Next: Functions](06_functions.md)
