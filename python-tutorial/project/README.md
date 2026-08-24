# 🎯 Capstone Project: Student Management System

This is a real, working command-line app that uses **every topic** from
this course. You'll build it in stages — each stage adds one new skill on
top of the last, exactly the way real software gets built.

## Why this project?

It touches everything:
- **Variables & data types** → storing student info
- **Operators** → calculating grades, pass/fail
- **Strings** → formatting names and reports
- **Data structures** → a list of dictionaries (or objects) holding students
- **Control flow** → menus, decisions, loops for repeated actions
- **Functions** → one function per action (add, view, delete, search)
- **OOP** → a `Student` class to represent each student cleanly
- **File handling** → saving/loading data so it survives closing the app
- **Exception handling** → surviving bad input without crashing
- **Comprehensions** → quick filtering/reporting
- **NumPy/Pandas** (optional stretch stage) → analyzing all scores at once

## How to work through it

Read [step_by_step_build.md](step_by_step_build.md) — it builds the project
in 6 versions, from the simplest possible thing to the full app. Type each
version yourself, run it, understand it, THEN move to the next version.
Don't jump straight to the final file — you'll learn far less that way.

The finished, complete version is in [student_manager.py](student_manager.py)
— use it to check your work or as a reference, not as a shortcut to copy
before you've built your own.

## After this project — ideas to extend it yourself

Once it works, try adding these on your own (this is how real learning
happens — by extending something that already works):
- Add an `update_student()` feature to edit existing records
- Add sorting: view students sorted by score, highest first
- Add a class average calculator using NumPy
- Export the student list as a CSV report using Pandas
- Add input validation: no negative scores, no empty names
- Turn it into a simple Flask web app (a great "next course" topic)

---
➡ [Start building: step_by_step_build.md](step_by_step_build.md)
