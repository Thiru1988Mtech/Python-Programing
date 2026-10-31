# 02 — Operators (from absolute zero)

## 1. Real-life analogy

Think of operators as **tools on a calculator and a judge's gavel combined**.
Some tools do math (`+ - * /`), and others make a *judgment call* — true or
false, yes or no (`== > < and or`).

## 2. Arithmetic operators — the "calculator" tools

Let's go one at a time, super slowly.

```python
a = 10
b = 3

print(a + b)   # 13  -> addition: put a and b together
print(a - b)   # 7   -> subtraction: take b away from a
print(a * b)   # 30  -> multiplication: repeat a, b times
print(a / b)   # 3.333333333333335 -> division: split a into b equal parts (ALWAYS gives a decimal)
print(a // b)  # 3   -> floor division: division but DROP the decimal part
print(a % b)   # 1   -> modulus: the LEFTOVER after dividing (the remainder)
print(a ** b)  # 1000 -> power: a multiplied by itself b times (10*10*10)
```

### Deep dive on `%` (modulus) — this confuses every beginner at first

Think of modulus as: **"if I split this into groups, what's left over?"**

Real-life example: You have 10 candies and want to give them to 3 friends
equally.
- Each friend gets `10 // 3` = 3 candies (floor division: whole groups)
- You have `10 % 3` = 1 candy left over (modulus: the remainder)

**Most common real use of `%`: checking even or odd.**
```python
number = 7
if number % 2 == 0:      # "if there's NO remainder when divided by 2"
    print("Even")
else:
    print("Odd")
```
Trace it: `7 % 2` → 7 divided by 2 is 3 groups with 1 left over → `1`.
Is `1 == 0`? No. So it goes to `else` → prints "Odd". ✅

## 3. Comparison operators — the "judge" tools

These ALWAYS give back only `True` or `False` — nothing else.

```python
a = 10
b = 3

print(a == b)   # False -> "is a EQUAL TO b?" (double = for comparing!)
print(a != b)   # True  -> "is a NOT equal to b?"
print(a > b)    # True  -> "is a greater than b?"
print(a < b)    # False -> "is a less than b?"
print(a >= 10)  # True  -> "is a greater than or equal to 10?"
print(a <= 5)   # False -> "is a less than or equal to 5?"
```

> 🧠 THE #1 beginner mistake: confusing `=` and `==`.
> - `=` → **stores** a value into a box (an action: "put this in")
> - `==` → **compares** two values (a question: "are these the same?")
>
> `if age = 18:` → ❌ this will ERROR (you can't "store" inside an if-check)
> `if age == 18:` → ✅ this asks "is age equal to 18?"

## 4. Logical operators — combining multiple judgments

Real life: *"I'll go to the beach if it's sunny AND it's the weekend."*
That's TWO conditions joined together.

```python
is_sunny = True
is_weekend = False

print(is_sunny and is_weekend)  # False -> BOTH must be True; one is False, so whole thing is False
print(is_sunny or is_weekend)   # True  -> AT LEAST ONE must be True; is_sunny is True, so True
print(not is_sunny)             # False -> flips True into False (and vice versa)
```

Think of `and` as a strict parent: **everything must be true.**
Think of `or` as a relaxed friend: **just one thing being true is enough.**
Think of `not` as an opposite-button: **flips whatever it's given.**

### Combining comparison + logical (this is how real decisions get made)
```python
age = 20
has_ticket = True

# "Can enter if age is 18+ AND has a ticket"
can_enter = age >= 18 and has_ticket
print(can_enter)   # True
```

## 5. Assignment operators — quick "update the box" shortcuts

```python
score = 10
score = score + 5    # long way: take what's in score, add 5, put it back
print(score)          # 15

score = 10
score += 5            # short way: exact same thing as above
print(score)          # 15

score -= 3    # same as score = score - 3
score *= 2    # same as score = score * 2
score /= 4    # same as score = score / 4
```

## 6. Full worked example — a mini "can I drive" checker

```python
age = int(input("Enter your age: "))
has_license = input("Do you have a license? (yes/no): ")

# Step 1 (plain English): "You can drive if age is 18+ AND you have a license"
can_drive = age >= 18 and has_license == "yes"

print("Can you drive legally?", can_drive)
```

Trace through with `age = 20`, `has_license = "yes"`:
1. `age >= 18` → `20 >= 18` → `True`
2. `has_license == "yes"` → `"yes" == "yes"` → `True`
3. `True and True` → `True`
4. Output: `Can you drive legally? True`

## 7. Common mistakes

```python
if age = 18:     # ❌ SyntaxError - you can't "assign" inside a condition
```
Fix: use `==` for comparing.

```python
print(5 = 5)     # ❌ makes no sense - can't "assign into" a number 5
```

## 8. Practice

1. Write code that checks if a number is divisible by both 4 and 6 (use
   `%` and `and`).
2. Ask the user for their weight (kg) and height (m), calculate BMI using
   `weight / (height ** 2)`, and print it.
3. Write `is_teenager = age >= 13 and age <= 19` and test it with a few
   different ages.
4. Predict the output of `17 % 5` on paper first, then run it and check.

---
⬅ [Previous: Python Basics](01_python_basics.md) | ➡ [Next: Strings](03_strings.md)
