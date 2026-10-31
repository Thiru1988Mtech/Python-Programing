# 00 — Start Here: How a Computer "Thinks" (Absolute Zero Level)

> Read this before anything else. Even if you've never touched code, by
> the end of this page you will understand what programming actually *is*.

## 1. What is a program, really?

Imagine you're teaching a **very obedient but very literal robot** to make
a cup of tea. The robot does *exactly* what you say, in *exactly* the
order you say it, and nothing more.

If you say "make tea," the robot stares blankly — that's not specific
enough. You have to say:

```
1. Pick up the kettle
2. Fill it with water
3. Turn on the kettle
4. Wait until the water boils
5. Pour water into the cup
6. Add a tea bag
7. Wait 3 minutes
8. Remove the tea bag
```

**That list of exact, ordered steps is a program.** A programming language
(like Python) is just a way of writing those steps so a computer (the
robot) can understand them precisely.

This is the single most important idea in all of programming:

> **Programming = breaking a big problem into tiny, exact, ordered steps.**

Everything you learn from here on is just new *vocabulary* for describing
steps — nothing more.

## 2. Why Python?

Python is written to look almost like English. Compare:

- English: "If the age is 18 or more, print Adult"
- Python: `if age >= 18: print("Adult")`

That's it. Python is one of the easiest languages to read because it was
designed to be readable by humans first, computers second.

## 3. How code actually runs (line by line)

A computer reads your code **from top to bottom, one line at a time**,
like reading a recipe. It does NOT know what's coming next until it gets
there. This means:

- Order matters. If line 1 uses something defined in line 5, it will fail
  — because line 5 hasn't happened yet.
- The computer has **zero common sense**. If you misspell a word or forget
  a symbol, it will not "guess" what you meant — it will simply refuse to
  run and show an **error**.

### Your first program, traced step-by-step

```python
print("Hello, World!")
```

What happens when you run this:
1. Python sees the word `print` → "Oh, I need to display something on
   screen."
2. It sees `(` → "Ok what's inside the parentheses is what I display."
3. It sees `"Hello, World!"` → "That's text (a string) — display it exactly."
4. It sees `)` → "End of instruction."
5. Output appears: `Hello, World!`

Try changing the text inside the quotes and running it again. This is how
you'll learn everything — **change one small thing, run it, see what
happens.**

## 4. Errors are not scary — they are the computer talking to you

New programmers panic when they see red error text. Don't. An error is the
computer saying: *"I don't understand this specific line, here's exactly
why."*

Example:
```python
print("Hello"
```
Output:
```
SyntaxError: '(' was never closed
```
Translation: *"You opened a bracket `(` but never closed it with `)`."*
That's all it means. Fix it, run again.

> 🧠 Golden rule: **Always read the LAST line of an error message first.**
> That's usually where the actual explanation is.

## 5. The mindset for every single topic ahead

For every new concept in this course, ask these 3 questions, in order:

1. **What real-life problem does this solve?** (find an everyday analogy)
2. **What are the exact tiny steps to solve it?** (write it in plain
   English first — no code yet)
3. **How do I say those exact steps in Python?** (code comes last, not
   first)

If you always do step 1 and 2 before step 3, you will never feel "lost" —
because you'll already understand the logic before you see any code.

## 6. Setting up your coding environment (do this now)

1. Go to [python.org/downloads](https://www.python.org/downloads/) and
   install Python (click the big yellow "Download Python" button).
2. During install on Windows, **tick the box "Add Python to PATH"** — this
   is the #1 setup mistake beginners make.
3. Open a terminal / command prompt and type:
   ```
   python --version
   ```
   If it shows a version number like `Python 3.12.0`, you're ready.
4. Create a folder on your computer called `python-practice`.
5. Inside it, create a file called `day1.py` and put:
   ```python
   print("I just wrote my first Python file!")
   ```
6. Run it:
   ```
   python day1.py
   ```

If you saw the message printed — congratulations, you are now a
programmer. Everything from here is just building on this exact loop:
**write → run → see result → adjust.**

---
➡ [Next: Python Basics](topics/01_python_basics.md)
