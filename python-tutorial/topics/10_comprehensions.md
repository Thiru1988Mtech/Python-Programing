# 10 — Comprehensions & Expressions (from absolute zero)

## 1. Real-life analogy

Imagine an assembly line: raw items go in one end, get transformed, and
come out the other end as a new finished list. A comprehension is Python's
way of describing that ENTIRE assembly line in a single line of code.

## 2. Always start with the loop version first (never skip this step)

**Goal: "square every number in this list"**

Step 1 — plain English: *"For each number, calculate its square, and
collect all the results into a new list."*

Step 2 — normal loop version (write this FIRST, always):
```python
numbers = [1, 2, 3, 4, 5]
squares = []                    # start with an empty list

for n in numbers:
    squares.append(n * n)       # transform each item and add to the new list

print(squares)   # [1, 4, 9, 16, 25]
```

Step 3 — now compress into a list comprehension (same logic, one line):
```python
squares = [n * n for n in numbers]
print(squares)   # [1, 4, 9, 16, 25]
```

Read the comprehension left to right as: *"Give me `n * n`, for every `n`
found in `numbers`."*

## 3. Adding a filter — the `if` part

**Goal: "keep only the even numbers"**

Loop version first:
```python
numbers = [1, 2, 3, 4, 5, 6]
evens = []
for n in numbers:
    if n % 2 == 0:
        evens.append(n)
print(evens)   # [2, 4, 6]
```

Comprehension version:
```python
evens = [n for n in numbers if n % 2 == 0]
print(evens)   # [2, 4, 6]
```
Read as: *"Give me `n`, for every `n` in numbers, BUT ONLY IF `n % 2 == 0`."*

## 4. Combining transform + filter together

```python
numbers = [1, 2, 3, 4, 5, 6]
even_squares = [n * n for n in numbers if n % 2 == 0]
print(even_squares)   # [4, 16, 36]
```
Read as: *"Give me `n * n`, for every `n` in numbers, only if `n` is even."*

## 5. Dictionary comprehensions — the same idea, for dictionaries

Loop version first:
```python
names = ["asha", "ravi", "meena"]
name_lengths = {}
for name in names:
    name_lengths[name] = len(name)
print(name_lengths)
```

Comprehension version:
```python
name_lengths = {name: len(name) for name in names}
print(name_lengths)   # {'asha': 4, 'ravi': 4, 'meena': 5}
```

## 6. Set comprehensions

```python
words = ["apple", "banana", "apple", "cherry"]
unique_lengths = {len(w) for w in words}
print(unique_lengths)   # {5, 6}
```

## 7. Conditional (ternary) expressions — a mini if/else in one line

```python
age = 20
# Long way:
if age >= 18:
    status = "Adult"
else:
    status = "Minor"

# Short way (ternary expression):
status = "Adult" if age >= 18 else "Minor"
print(status)   # Adult
```
Read right to left through the middle: *"'Adult' IF `age >= 18` ELSE
'Minor'."*

## 8. Full worked example — processing a list of student scores

```python
scores = [45, 88, 92, 55, 79, 60, 30]

# 1. Get pass/fail status for each score (ternary inside a comprehension)
statuses = ["Pass" if score >= 50 else "Fail" for score in scores]
print(statuses)

# 2. Get only the passing scores
passing_scores = [score for score in scores if score >= 50]
print(passing_scores)

# 3. Build a dictionary of score -> status
score_status = {score: ("Pass" if score >= 50 else "Fail") for score in scores}
print(score_status)
```

## 9. When NOT to use a comprehension

If the logic needs multiple steps or is hard to read in one line, just use
a normal loop instead — comprehensions should make code CLEARER, not more
confusing. If you (or someone else) can't understand it at a glance,
that's a sign to write it as a full loop.

## 10. Practice

1. Write a list comprehension for cubes (`n**3`) of numbers 1 to 10.
2. Filter `["cat", "elephant", "dog", "giraffe"]` to only words longer than
   4 letters.
3. Write a dictionary comprehension mapping numbers 1-5 to their squares.
4. Given `temperatures = [15, 22, 35, 8, 40]`, use a comprehension with a
   ternary to label each as `"Hot"` if `>= 30` else `"Not Hot"`.

---
⬅ [Previous: Exception Handling](09_exception_handling.md) | ➡ [Next: NumPy](11_numpy.md)
