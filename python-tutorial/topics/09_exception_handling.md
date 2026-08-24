# 09 — Exception Handling (from absolute zero)

## 1. Real-life analogy

Imagine driving a car with airbags. You don't PLAN to crash, but if you
do, the airbag protects you instead of the situation becoming fatal.
Exception handling is your program's "airbag" — it catches unexpected
problems so the whole program doesn't crash and burn.

## 2. What is an exception exactly?

An exception is an error that happens WHILE the program is running (not a
typo caught before running, but a real "something went wrong right now").

```python
number = int(input("Enter a number: "))   # if user types "hello", this CRASHES
print(10 / number)                         # if user types 0, this ALSO crashes
```
Without handling, either of these mistakes stops your entire program dead.

## 3. `try` / `except` — the safety net, step by step

```python
try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print("Result:", result)
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("You can't divide by zero!")
```

Read as: *"TRY this risky code. IF a ValueError happens (bad conversion),
do this instead. IF a ZeroDivisionError happens, do that instead."*

**Trace it with input `"hello"`:**
1. `int("hello")` fails immediately → Python raises a `ValueError`
2. Python jumps STRAIGHT to `except ValueError:` skipping the rest of `try`
3. Prints "That's not a valid number!" — program continues normally after

**Trace it with input `"0"`:**
1. `int("0")` succeeds → `number = 0`
2. `10 / 0` fails → Python raises a `ZeroDivisionError`
3. Jumps to `except ZeroDivisionError:` → prints "You can't divide by zero!"

## 4. `finally` — code that ALWAYS runs, error or not

```python
try:
    number = int(input("Enter a number: "))
    print(10 / number)
except ZeroDivisionError:
    print("Can't divide by zero!")
finally:
    print("Thanks for using the calculator!")   # runs NO MATTER WHAT happens above
```
Use `finally` for cleanup actions, like closing a file or a database
connection — things that must happen regardless of success or failure.

## 5. Catching ANY error (use only when you truly don't know what might fail)

```python
try:
    data = [1, 2, 3]
    print(data[10])
except Exception as e:      # 'Exception' catches almost anything
    print("Something went wrong:", e)
```
> 🧠 Prefer catching SPECIFIC errors (`ValueError`, `ZeroDivisionError`,
> etc.) when you can predict them — it makes your code more precise and
> easier to debug. Only use the broad `Exception` catch-all as a last
> resort/safety net.

## 6. Raising your OWN errors — enforcing rules in your own functions

```python
def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient funds!")   # you can trigger errors deliberately
    return balance - amount

try:
    new_balance = withdraw(100, 150)
except ValueError as e:
    print("Error:", e)     # Error: Insufficient funds!
```
This is how real applications enforce business rules — instead of letting
bad data silently continue, you stop it immediately with a clear message.

## 7. Full worked example — safe file reading + safe division calculator

```python
def safe_divide():
    try:
        num1 = float(input("Enter numerator: "))
        num2 = float(input("Enter denominator: "))
        result = num1 / num2
        print(f"Result: {result}")
    except ValueError:
        print("Please enter valid numbers.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    finally:
        print("Calculation attempt finished.")

def read_config():
    try:
        with open("config.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("Config file not found — using default settings.")

safe_divide()
read_config()
```

## 8. Common mistakes

```python
try:
    print(10 / 0)
except:              # ⚠️ bare 'except' catches EVERYTHING, even typos in your own code!
    print("Error")    # This can HIDE real bugs. Always name the specific error type.
```

## 9. Practice

1. Write code that asks for two numbers and divides them, handling both
   `ValueError` and `ZeroDivisionError` with clear messages.
2. Write `get_item(my_list, index)` that safely returns the item at that
   index, or `"Invalid index"` on `IndexError`.
3. Use `raise` inside a function `set_age(age)` to raise a `ValueError` if
   age is negative.
4. Wrap the CSV-reading code from Topic 08 in a `try/except` to handle a
   missing file gracefully.

---
⬅ [Previous: File & Data Handling](08_file_data_handling.md) | ➡ [Next: Comprehensions & Expressions](10_comprehensions.md)
