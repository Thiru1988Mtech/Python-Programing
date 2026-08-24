# 13 — Advanced Python (from absolute zero)

## 1. Lambda functions — tiny, throwaway functions

**Real-life analogy:** a lambda is like a sticky note version of a
function — quick, disposable, used once, not meant to be a permanent
recipe card.

```python
# Normal function
def square(x):
    return x * x

# Same thing as a lambda
square_lambda = lambda x: x * x
print(square_lambda(5))   # 25
```
Read `lambda x: x * x` as: *"a mini function that takes `x` and gives back
`x * x`, with no name needed."*

**Most common real use — as a sorting rule:**
```python
students = [("Asha", 88), ("Ravi", 92), ("Meena", 79)]

students.sort(key=lambda student: student[1])   # sort by the SECOND item (score)
print(students)   # [('Meena', 79), ('Asha', 88), ('Ravi', 92)]
```
Read `key=lambda student: student[1]` as: *"when comparing items to sort
them, look at `student[1]` (the score) instead of the whole tuple."*

## 2. `*args` and `**kwargs` — functions that accept ANY number of inputs

**`*args`** — accepts any number of plain (positional) values, bundled into
a tuple:
```python
def total(*args):
    print(args)          # (1, 2, 3) -> a tuple of everything passed in
    return sum(args)

print(total(1, 2, 3))         # 6
print(total(10, 20, 30, 40))  # 100 -> works with ANY number of arguments
```

**`**kwargs`** — accepts any number of named values, bundled into a
dictionary:
```python
def show_profile(**kwargs):
    print(kwargs)     # {'name': 'Asha', 'age': 25, 'city': 'Chennai'}
    for key, value in kwargs.items():
        print(f"{key}: {value}")

show_profile(name="Asha", age=25, city="Chennai")
```

## 3. Generators — producing values one at a time (memory-efficient)

**Real-life analogy:** a normal list is like baking ALL the cookies at
once and stacking them on a plate (uses lots of counter space). A
generator is like a cookie that pops out of the oven only when you ask for
the next one — nothing is made until it's needed.

```python
def count_up_to(n):
    count = 1
    while count <= n:
        yield count      # 'yield' pauses here and hands back a value,
        count += 1        # then RESUMES from this exact spot next time

for number in count_up_to(5):
    print(number)   # 1 2 3 4 5, produced one at a time
```
The difference from `return`: `return` ends the function completely.
`yield` pauses it, remembering exactly where it left off, ready to
continue on the next request.

## 4. Decorators — wrapping extra behavior around a function

**Real-life analogy:** a decorator is like gift-wrapping a present — the
present (your original function) doesn't change, but it gets extra
paper/ribbon (behavior) added around it.

```python
def my_decorator(func):
    def wrapper():
        print("Before the function runs")
        func()
        print("After the function runs")
    return wrapper

@my_decorator            # this line says "wrap say_hello with my_decorator"
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Before the function runs
# Hello!
# After the function runs
```
A very common real use: timing how long a function takes to run, or
logging every time a function is called, without editing the function
itself.

## 5. Modules — splitting code across multiple files

As programs grow, you don't want everything in one giant file. A module is
just a `.py` file whose functions/classes you can reuse elsewhere.

```python
# In a file called helpers.py:
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b
```
```python
# In your main.py file, in the SAME folder:
import helpers

print(helpers.add(2, 3))         # 5
print(helpers.multiply(4, 5))    # 20

# Or import just what you need:
from helpers import add
print(add(10, 20))    # 30
```

## 6. Full worked example — combining everything

```python
import time

def timer(func):                    # a decorator that measures execution time
    def wrapper(*args, **kwargs):   # accepts ANY function's arguments
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_square(n):
    time.sleep(1)     # pretend this takes time
    return n * n

print(slow_square(5))
```

## 7. Common mistakes

```python
def total(*args):
    return sum(args)

total(1, 2, 3)   # forgot to catch the return value or print it -> nothing shows
```

```python
def count_up_to(n):
    count = 1
    while count <= n:
        return count     # ❌ used 'return' instead of 'yield' -> stops after ONE value
        count += 1
```

## 8. Practice

1. Write a lambda that returns the cube of a number, and test it.
2. Write `total_price(*args)` that sums any number of prices.
3. Write a generator `even_numbers(n)` that yields even numbers up to `n`.
4. Write a decorator `log_call` that prints `"Calling <function name>..."`
   before running any function it's applied to.

---
⬅ [Previous: Pandas](12_pandas.md) | 🏠 [Back to index](../README.md)

## 🎉 You now know the full roadmap — time to build!
Go to the [Capstone Project](../project/README.md) to build a real
Student Management System using EVERY topic you just learned.
