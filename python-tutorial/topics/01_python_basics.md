# 01 — Python Basics (from absolute zero)

> If you haven't read [00 — Start Here](../00_start_here.md), do that first.

## 1. The real-life analogy

Imagine your bedroom. You have labeled boxes: one box says "Photos," another
says "Winter Clothes," another says "Documents." You put specific things
inside each box, and later you can open the box labeled "Photos" to get
your photos back — you don't need to remember exactly where each photo is,
just the box's label.

**A variable is exactly this: a labeled box that stores one piece of
information**, so your program can find and reuse it later just by its name.

## 2. Step-by-step: creating your first variable

Let's build understanding one tiny step at a time.

**Step 1 — Storing a value**
```python
age = 25
```
Read this out loud as: *"Create a box labeled `age`, and put the number 25
inside it."*

**Step 2 — Using the value**
```python
print(age)
```
Read as: *"Open the box labeled `age`, and show me what's inside."*
Output: `25`

**Step 3 — Changing the value**
```python
age = 26
print(age)
```
The box still has the same label, but now we replaced what's inside.
Output: `26`

> 🧠 Important: `age = 25` does NOT mean "age equals 25" like in math class.
> It means **"put 25 into the box called age."** The `=` sign means "store
> into," not "is equal to." (You'll learn the "is equal to" symbol — `==`
> — in the next topic.)

## 3. The four basic types of boxes (data types)

Every box also has a "kind" of thing it holds. Python figures this out
automatically based on what you put in.

| Type | What it holds | Example | Real-life analogy |
|------|---------------|---------|--------------------|
| `int` | whole numbers | `age = 25` | counting apples: 1, 2, 3 |
| `float` | decimal numbers | `price = 19.99` | a weighing scale reading |
| `str` | text (letters/words) | `name = "Asha"` | a name tag |
| `bool` | True or False only | `is_raining = True` | a light switch: on/off |

**Try this and read the output carefully:**
```python
age = 25
price = 19.99
name = "Asha"
is_raining = True

print(name, "is", age, "years old.")
print("Type of age:", type(age))
print("Type of price:", type(price))
print("Type of name:", type(name))
print("Type of is_raining:", type(is_raining))
```

**Output:**
```
Asha is 25 years old.
Type of age: <class 'int'>
Type of price: <class 'float'>
Type of name: <class 'str'>
Type of is_raining: <class 'bool'>
```

`type()` is like asking "what kind of box is this?" — very useful when
you're confused about what something is.

## 4. Naming your boxes (variable naming rules)

Rules (the computer WILL error if you break these):
- Must start with a letter or underscore: `age`, `_age` ✅ — not `2age` ❌
- No spaces: use `first_name`, not `first name` ❌
- Case-sensitive: `Age` and `age` are two *different* boxes
- Cannot be a Python reserved word: not `print = 5` ❌ (since `print` is
  already a built-in tool)

Good habits (not required, but professional):
- Use lowercase with underscores: `first_name`, `total_price`
- Make names descriptive: `age` not `a`, `total_score` not `ts`

## 5. Comments — notes to yourself (and others)

```python
# This is a comment. Python completely ignores this line.
age = 25  # you can also put a comment after code, on the same line
```
Use comments to explain *why* you did something — future-you (or someone
reading your GitHub code) will thank you.

## 6. Getting input from a real user

So far we've only hard-coded values. Real programs ask the *user* for
information.

```python
name = input("What is your name? ")   # input() always returns TEXT (a string)
print("Hello,", name)

age_text = input("How old are you? ")
age = int(age_text)     # convert the text "25" into the number 25
print("Next year you'll be", age + 1)
```

> 🧠 Common beginner mistake: `input()` ALWAYS gives you text, even if the
> user types a number. If you try `age_text + 1` without converting with
> `int()` first, Python will error, because you can't add a number to text.

## 7. Full worked example (put all pieces together)

```python
# A tiny program that introduces itself using variables

name = "Asha"
age = 25
city = "Chennai"
is_learning_python = True

print("=== My Profile ===")
print("Name:", name)
print("Age:", age)
print("City:", city)
print("Learning Python:", is_learning_python)

# Update a value
age = age + 1
print("Next year, I will be", age)
```

**Trace it in your head before running:**
1. Four boxes get created: `name`, `age`, `city`, `is_learning_python`.
2. Five `print()` lines display their contents in order, top to bottom.
3. `age = age + 1` opens the `age` box, takes out 25, adds 1, puts 26 back
   in the same box.
4. Last line shows the new value.

## 8. Common mistakes beginners make (and how to read the error)

```python
print(Age)          # NameError: name 'Age' is not defined
```
Meaning: you tried to open a box called `Age` (capital A) but only `age`
(lowercase) exists. Python is case-sensitive.

```python
print("My age is " + 25)   # TypeError: can only concatenate str (not "int") to str
```
Meaning: you tried to glue text and a number together with `+`. Fix it by
converting: `print("My age is " + str(25))` or better, use an f-string
(you'll learn this in Strings, Topic 03).

## 9. Practice (do NOT skip this)

1. Create variables for `favorite_food`, `favorite_number`, and
   `likes_coding` (bool), then print all three with labels.
2. Ask the user for their name using `input()` and print
   `"Welcome, <name>!"`.
3. Ask the user for two numbers using `input()`, convert both with `int()`,
   add them, and print the result.
4. Break something on purpose: remove a closing quote from a string and
   run the code. Read the error message. Fix it.

---
⬅ [Back to index](../README.md) | ➡ [Next: Operators](02_operators.md)
