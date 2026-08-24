# 06 — Functions (from absolute zero)

## 1. Real-life analogy

A function is like a **kitchen recipe card**. You write the recipe ONCE
("Recipe: Make Tea"). Then, anytime you want tea, you just say "make tea"
— you don't rewrite the whole recipe from scratch every time. You can also
give the recipe different **ingredients** (inputs) and get slightly
different results, and it **hands you back** a finished cup (output).

## 2. Defining and calling a function — the two separate steps

**Step 1 — Defining** (writing the recipe, nothing happens yet):
```python
def greet():
    print("Hello!")
```
`def` means "I'm about to define a function." `greet` is its name. The
empty `()` means "it takes no ingredients (inputs)." Nothing prints yet —
you've only WRITTEN the recipe, not used it.

**Step 2 — Calling** (actually using the recipe):
```python
greet()    # NOW it runs -> Output: Hello!
greet()    # can call it again as many times as you want
greet()
```

> 🧠 Beginner confusion: defining a function does NOT run it. You must
> "call" it (write its name + parentheses) to actually execute the code
> inside.

## 3. Parameters — giving the recipe ingredients (inputs)

```python
def greet(name):          # 'name' is a PARAMETER -> a placeholder for future input
    print(f"Hello, {name}!")

greet("Asha")   # 'Asha' is the ARGUMENT -> the actual value plugged in
greet("Ravi")   # same function, different result
```

**Multiple parameters:**
```python
def introduce(name, age):
    print(f"{name} is {age} years old.")

introduce("Asha", 25)
introduce("Ravi", 22)
```

> 🧠 Order matters! `introduce("Asha", 25)` puts "Asha" into `name` and 25
> into `age`, matched by POSITION.

## 4. `return` — getting a value BACK from the function

`print()` just displays something on screen — it doesn't give the value
back to use later. `return` actually hands the result back so you can
store it or use it further.

```python
def add(a, b):
    result = a + b
    return result       # hands the sum back to whoever called this function

total = add(5, 3)       # 'total' now holds the value 8
print(total)            # 8
print(add(10, 20))      # 30 -> you can also use it directly inside print()

doubled_total = add(5, 3) * 2    # you can do MORE math with the returned value
print(doubled_total)             # 16
```

**The difference between `print` and `return` (very important):**
```python
def add_v1(a, b):
    print(a + b)    # only DISPLAYS it, gives nothing back

def add_v2(a, b):
    return a + b    # HANDS BACK the value to be used further

x = add_v1(2, 3)   # screen shows: 5.  But x is actually None (nothing useful)!
y = add_v2(2, 3)   # screen shows NOTHING. But y is actually 5, ready to use!

print(x)   # None
print(y)   # 5
```

## 5. Default parameter values

```python
def power(base, exponent=2):     # exponent defaults to 2 if not given
    return base ** exponent

print(power(4))       # 16  -> uses the default exponent=2 -> 4**2
print(power(4, 3))    # 64  -> overrides default -> 4**3
```

## 6. Functions calling other functions (building blocks)

```python
def calculate_area(length, width):
    return length * width

def describe_room(length, width):
    area = calculate_area(length, width)     # reusing another function!
    return f"The room area is {area} square units"

print(describe_room(5, 4))   # The room area is 20 square units
```
This is exactly how real software is built: small, simple functions,
combined into bigger ones.

## 7. Full worked example — mini calculator

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero!"
    return a / b

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Choose operation (+, -, *, /): ")

if operation == "+":
    print("Result:", add(num1, num2))
elif operation == "-":
    print("Result:", subtract(num1, num2))
elif operation == "*":
    print("Result:", multiply(num1, num2))
elif operation == "/":
    print("Result:", divide(num1, num2))
else:
    print("Invalid operation")
```

## 8. Variable scope — where a variable "lives"

```python
def my_function():
    local_var = "I only exist inside this function"
    print(local_var)

my_function()
print(local_var)   # ❌ NameError! local_var doesn't exist out here
```
Think of it like this: whatever gets created INSIDE a function's recipe
card stays in the kitchen — it doesn't automatically appear in your dining
room (the rest of your program).

## 9. Common mistakes

```python
def greet(name):
    print(f"Hello {name}")

greet()   # ❌ TypeError: greet() missing 1 required positional argument: 'name'
```
Fix: always provide required arguments, or give the parameter a default
value.

```python
def add(a, b):
    a + b          # forgot 'return' -> function gives back None by default!

result = add(2, 3)
print(result)   # None  (not 5!)
```

## 10. Practice

1. Write `square(n)` that returns `n * n`. Test with a few numbers.
2. Write `is_adult(age)` returning `True`/`False` based on `age >= 18`.
3. Write `greet_user(name, greeting="Hi")` with a default value, call it
   both with and without the second argument.
4. Write a function `calculate_total(price, quantity, tax_rate=0.05)` that
   returns the total cost including tax.

---
⬅ [Previous: Control Flow](05_control_flow.md) | ➡ [Next: Object-Oriented Python](07_oop.md)
