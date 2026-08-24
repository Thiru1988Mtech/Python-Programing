# Building the Student Management System — Step by Step

We'll build this in 6 versions. Each version is a COMPLETE, runnable
program — copy each one into its own file (`v1.py`, `v2.py`, etc.), run it,
play with it, and understand why each new piece was added before moving on.

---

## Version 1 — Just variables and printing (Topics 01–03)

**Goal:** store ONE student's info and print a report. No lists, no
functions yet — just the absolute basics.

```python
name = "Asha"
age = 25
score = 88

print(f"Student: {name}")
print(f"Age: {age}")
print(f"Score: {score}")

if score >= 50:
    print("Status: Pass")
else:
    print("Status: Fail")
```

**What to notice:** this only works for ONE student. If we wanted 5
students, we'd need to copy-paste this 5 times — clearly a problem we need
to solve next.

---

## Version 2 — A list of dictionaries + a loop (Topics 04–05)

**Goal:** store MULTIPLE students, and loop through all of them.

```python
students = [
    {"name": "Asha", "age": 25, "score": 88},
    {"name": "Ravi", "age": 22, "score": 45},
    {"name": "Meena", "age": 28, "score": 79},
]

for student in students:
    status = "Pass" if student["score"] >= 50 else "Fail"
    print(f"{student['name']} (age {student['age']}) - Score: {student['score']} - {status}")
```

**What to notice:** now ANY number of students works, because the `for`
loop repeats the same logic for each one. But we still can't ADD a new
student while the program is running — everything is hard-coded. Let's fix
that next with functions and a menu.

---

## Version 3 — Functions + a menu loop (Topic 06)

**Goal:** let the user interactively add students and view them, using a
repeating menu (`while` loop) and separate functions for each action.

```python
students = []   # starts empty, grows as the user adds students

def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter age: "))
    score = float(input("Enter score: "))
    students.append({"name": name, "age": age, "score": score})
    print(f"{name} added!")

def view_students():
    if not students:
        print("No students yet.")
        return
    for student in students:
        status = "Pass" if student["score"] >= 50 else "Fail"
        print(f"{student['name']} (age {student['age']}) - Score: {student['score']} - {status}")

def main():
    while True:
        print("\n--- Student Management ---")
        print("1. Add student")
        print("2. View students")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

main()
```

**What to notice:** each menu action is its OWN function — this is exactly
how real apps are organized: one function per feature, called from a
central menu loop.

---

## Version 4 — Upgrade to a `Student` class (Topic 07)

**Goal:** replace the plain dictionary with a proper class, so each
student can have its own behavior (like calculating pass/fail itself).

```python
class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def status(self):
        return "Pass" if self.score >= 50 else "Fail"

    def report(self):
        return f"{self.name} (age {self.age}) - Score: {self.score} - {self.status()}"

students = []

def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter age: "))
    score = float(input("Enter score: "))
    students.append(Student(name, age, score))
    print(f"{name} added!")

def view_students():
    if not students:
        print("No students yet.")
        return
    for student in students:
        print(student.report())

def main():
    while True:
        print("\n--- Student Management ---")
        print("1. Add student")
        print("2. View students")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

main()
```

**What to notice:** `student.report()` reads much more cleanly than
rebuilding the same f-string everywhere. The LOGIC of "how to describe a
student" now lives inside the `Student` class itself, in one place.

---

## Version 5 — Save/load data with JSON + handle bad input (Topics 08–09)

**Goal:** don't lose all students when the program closes. Also, don't
crash if the user types text instead of a number.

```python
import json

class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def status(self):
        return "Pass" if self.score >= 50 else "Fail"

    def report(self):
        return f"{self.name} (age {self.age}) - Score: {self.score} - {self.status()}"

    def to_dict(self):              # convert to a plain dict, so JSON can save it
        return {"name": self.name, "age": self.age, "score": self.score}

FILE_NAME = "students.json"

def load_students():
    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)
            return [Student(s["name"], s["age"], s["score"]) for s in data]
    except FileNotFoundError:
        return []      # first time running -> no file yet, start empty

def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump([s.to_dict() for s in students], file)

def add_student(students):
    name = input("Enter student name: ").strip()
    try:
        age = int(input("Enter age: "))
        score = float(input("Enter score: "))
    except ValueError:
        print("Age must be a whole number and score must be a number. Try again.")
        return
    students.append(Student(name, age, score))
    save_students(students)
    print(f"{name} added and saved!")

def view_students(students):
    if not students:
        print("No students yet.")
        return
    for student in students:
        print(student.report())

def main():
    students = load_students()
    while True:
        print("\n--- Student Management ---")
        print("1. Add student")
        print("2. View students")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

main()
```

**What to notice:** `load_students()` runs once at the start, `save_students()`
runs every time data changes — so nothing is ever lost. The `try/except`
around age/score input means typing "abc" for age no longer crashes the
whole app.

---

## Version 6 — The full app (comprehensions + reporting)

This is the version in [student_manager.py](student_manager.py) — it adds:
- Search/filter using **comprehensions**
- A class average report
- Delete functionality
- Cleaner menu structure

Open that file now, read it top to bottom, and run it. By this point every
single line should be understandable to you, because you built up to it
piece by piece.

---
⬅ [Back to project overview](README.md)
