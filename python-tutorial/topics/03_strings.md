# 03 — Strings (from absolute zero)

## 1. Real-life analogy

A string is like a **row of numbered mailboxes on a street**, where each
mailbox holds exactly one letter (character) of your text. The numbering
starts at 0, not 1 — this is called "zero-indexing" and trips up every
beginner at first, so let's slow down here.

```
Text:      H   e   l   l   o
Position:  0   1   2   3   4
```

## 2. Creating and measuring a string

```python
name = "Hello"

print(len(name))   # 5 -> counts how many characters are in the mailboxes
```
Why does `len()` matter? It's how you know the "size" of your text — useful
for validation (e.g. "password must be at least 8 characters").

## 3. Indexing — grabbing ONE character by its position

```python
name = "Hello"

print(name[0])    # 'H'  -> the very first mailbox
print(name[1])    # 'e'  -> second mailbox
print(name[4])    # 'o'  -> fifth mailbox
print(name[-1])   # 'o'  -> negative counts from the END: -1 is always the last character
print(name[-2])   # 'l'  -> second-to-last
```

> 🧠 If you ask for `name[10]` on a 5-letter word, Python errors with
> `IndexError: string index out of range` — meaning "that mailbox doesn't
> exist, you went too far."

## 4. Slicing — grabbing a RANGE of characters

Format: `text[start : stop]` — Python grabs everything from `start` up to
(but NOT including) `stop`.

```python
name = "Hello World"

print(name[0:5])    # 'Hello'  -> positions 0,1,2,3,4 (5 is excluded!)
print(name[6:11])   # 'World'
print(name[:5])      # 'Hello'  -> leaving start empty means "from the beginning"
print(name[6:])      # 'World'  -> leaving stop empty means "to the very end"
print(name[:])       # 'Hello World' -> the whole thing
```

**Why does `stop` get excluded?** Think of it like cutting a ribbon: you
cut BEFORE the position number. `[0:5]` means "cut before mailbox 0 and
cut before mailbox 5" → you get exactly 5 characters (0,1,2,3,4).

## 5. Common string methods (built-in tools that come with every string)

```python
text = "  Hello World  "

print(text.upper())         # '  HELLO WORLD  '  -> all uppercase
print(text.lower())         # '  hello world  '  -> all lowercase
print(text.strip())         # 'Hello World'       -> removes extra spaces from ends
print(text.replace("World", "Python"))  # '  Hello Python  '
print(text.strip().split(" "))   # ['Hello', 'World'] -> breaks into a list by spaces
```

**Checking things inside a string:**
```python
email = "asha@example.com"

print("@" in email)          # True  -> "does @ exist somewhere in this text?"
print(email.startswith("asha"))  # True
print(email.endswith(".com"))    # True
```

## 6. Joining strings together (concatenation)

**Method 1 — the `+` operator (old-school, a bit clunky):**
```python
first = "Hello"
second = "World"
print(first + " " + second)   # Hello World
# note: you MUST manually add the space " " yourself
```

**Method 2 — f-strings (the modern, easiest, BEST way):**
```python
name = "Asha"
age = 25

print(f"My name is {name} and I am {age} years old")
# Output: My name is Asha and I am 25 years old
```
How to read this: the `f` before the quotes means "this string has live
variables inside curly braces `{}`." Python replaces `{name}` with
whatever is inside the `name` box, automatically.

You can even do math inside the curly braces:
```python
print(f"Next year I will be {age + 1}")
# Output: Next year I will be 26
```

## 7. Full worked example — a mini greeting card generator

```python
name = input("What's your name? ")
favorite_hobby = input("What's your favorite hobby? ")

name = name.strip().title()   # .title() makes "asha" into "Asha"

message = f"Hi {name}! It's awesome that you enjoy {favorite_hobby}."
print(message)
print(f"Your name has {len(name)} letters.")
print(f"Your name in uppercase: {name.upper()}")
```

## 8. Common mistakes

```python
age = 25
print("I am " + age)   # ❌ TypeError: can only concatenate str to str
```
Fix using f-string: `print(f"I am {age}")` ✅ — f-strings handle the
conversion for you automatically, which is another reason they're better
than `+`.

```python
name = "Hello"
name[0] = "J"   # ❌ TypeError: strings are immutable (cannot be changed piece by piece)
```
Strings can't be edited in place — you must create a NEW string instead:
```python
name = "J" + name[1:]   # 'Jello'
```

## 9. Practice

1. Store your full name, print just the first 3 letters using slicing.
2. Use an f-string to build a sentence describing yourself (name, age,
   city) in ONE print statement.
3. Take input from a user, `.strip()` it, and check if `"@"` is in it (like
   validating an email has an @ symbol).
4. Reverse a string using slicing: `text[::-1]` — try it and figure out why
   it works (hint: the third number in a slice is the "step").

---
⬅ [Previous: Operators](02_operators.md) | ➡ [Next: Data Structures](04_data_structures.md)
