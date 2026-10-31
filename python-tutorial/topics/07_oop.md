# 07 — Object-Oriented Python (from absolute zero)

## 1. Real-life analogy

Think of a **cookie cutter** (the class/blueprint) and the **actual
cookies** you cut out of dough (the objects). One cutter shape, but you can
make many cookies from it, and each cookie can be decorated differently
(different data) while sharing the same shape (same behavior).

## 2. Why not just use variables and functions for everything?

Imagine tracking 100 dogs using plain variables:
```python
dog1_name = "Rex"
dog1_age = 3
dog2_name = "Bella"
dog2_age = 5
# ...this gets messy FAST with more dogs and more properties
```
A class lets you bundle "name" and "age" together as ONE reusable "Dog"
blueprint, and create as many dogs as you want cleanly.

## 3. Building your first class, step by step

**Step 1 — define the blueprint:**
```python
class Dog:
    pass    # 'pass' means "empty for now, do nothing"
```

**Step 2 — give it a way to set up data when created (`__init__`):**
```python
class Dog:
    def __init__(self, name, age):
        self.name = name    # 'self.name' stores 'name' onto THIS specific dog
        self.age = age
```
- `__init__` runs AUTOMATICALLY the moment you create a new Dog.
- `self` means "this particular dog being created right now" — it's how
  each dog keeps its own separate name/age instead of sharing one.

**Step 3 — create actual dogs (objects) from the blueprint:**
```python
dog1 = Dog("Rex", 3)      # self=dog1, name="Rex", age=3
dog2 = Dog("Bella", 5)    # self=dog2, name="Bella", age=5

print(dog1.name)   # Rex
print(dog2.name)   # Bella  -> completely separate data, same blueprint!
```

## 4. Adding behavior (methods)

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):                      # a METHOD = a function that belongs to the class
        print(f"{self.name} says Woof!")

    def birthday(self):
        self.age += 1
        print(f"{self.name} is now {self.age} years old")

dog1 = Dog("Rex", 3)
dog1.bark()        # Rex says Woof!
dog1.birthday()    # Rex is now 4 years old
```

**Trace it:** `dog1.bark()` is really Python doing `bark(dog1)` behind the
scenes — `self` inside the method automatically becomes `dog1`, so
`self.name` becomes `dog1.name` → "Rex".

## 5. Inheritance — "IS-A" relationships (reusing a blueprint)

Real life: a Puppy IS-A Dog, but with some extra behavior.

```python
class Puppy(Dog):              # Puppy INHERITS everything from Dog
    def play(self):
        print(f"{self.name} is playing!")

puppy = Puppy("Max", 1)
puppy.bark()    # inherited from Dog -> Max says Woof!
puppy.play()    # Puppy's own new method -> Max is playing!
```
You got `bark()` and `birthday()` for FREE, without rewriting them,
because `Puppy(Dog)` means "build Puppy on top of Dog."

## 6. Overriding — customizing inherited behavior

```python
class Puppy(Dog):
    def bark(self):                       # SAME method name as in Dog
        print(f"{self.name} says Yip yip!")  # but different behavior

puppy = Puppy("Max", 1)
puppy.bark()   # Max says Yip yip!  (overridden version used instead)
```

## 7. Full worked example — a simple Bank Account class

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

account = BankAccount("Asha", 100)
account.deposit(50)      # Deposited 50. New balance: 150
account.withdraw(30)     # Withdrew 30. New balance: 120
account.withdraw(1000)   # Insufficient funds!
```

## 8. Common mistakes

```python
class Dog:
    def __init__(name, age):   # ❌ forgot 'self' as the first parameter
        ...
```
Every method inside a class MUST have `self` as its first parameter — it's
how Python knows which specific object to work with.

```python
dog1 = Dog("Rex", 3)
print(name)     # ❌ NameError -> must use dog1.name, not just 'name'
```

## 9. Practice

1. Create a `Car` class with `brand` and `speed`, plus a method `drive()`
   printing `"<brand> is driving at <speed> km/h"`.
2. Create a `SportsCar` class inheriting from `Car`, adding a `turbo()`
   method.
3. Create a `Student` class with `name` and a list of `grades`. Add a
   method `average()` that returns the average of the grades list.

---
⬅ [Previous: Functions](06_functions.md) | ➡ [Next: File & Data Handling](08_file_data_handling.md)
