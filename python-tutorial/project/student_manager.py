"""
Student Management System — Final Version (v6)
Built by combining every topic from the course:
variables, operators, strings, data structures, control flow,
functions, OOP, file handling, exception handling, comprehensions.

Run with: python student_manager.py
"""

import json

FILE_NAME = "students.json"


class Student:
    """Represents a single student and their own behavior."""

    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def status(self):
        return "Pass" if self.score >= 50 else "Fail"

    def report(self):
        return (f"{self.name} (age {self.age}) - "
                f"Score: {self.score} - {self.status()}")

    def to_dict(self):
        return {"name": self.name, "age": self.age, "score": self.score}


def load_students():
    """Load saved students from disk, or start fresh if no file exists."""
    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)
            return [Student(s["name"], s["age"], s["score"]) for s in data]
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Warning: saved file was corrupted, starting fresh.")
        return []


def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump([s.to_dict() for s in students], file)


def add_student(students):
    name = input("Enter student name: ").strip().title()
    if not name:
        print("Name cannot be empty.")
        return

    try:
        age = int(input("Enter age: "))
        score = float(input("Enter score: "))
    except ValueError:
        print("Age must be a whole number and score must be a number.")
        return

    if age <= 0 or score < 0 or score > 100:
        print("Age must be positive and score must be between 0-100.")
        return

    students.append(Student(name, age, score))
    save_students(students)
    print(f"✅ {name} added and saved!")


def view_students(students):
    if not students:
        print("No students yet. Add one first!")
        return
    print("\n--- All Students ---")
    for student in students:
        print(student.report())


def search_student(students):
    keyword = input("Enter name (or part of it) to search: ").strip().lower()
    # comprehension: filter students whose name contains the keyword
    matches = [s for s in students if keyword in s.name.lower()]

    if not matches:
        print("No matching students found.")
        return
    print(f"\n--- Search results for '{keyword}' ---")
    for student in matches:
        print(student.report())


def delete_student(students):
    name = input("Enter the exact name of the student to delete: ").strip().title()
    for student in students:
        if student.name == name:
            students.remove(student)
            save_students(students)
            print(f"🗑️ {name} deleted.")
            return
    print(f"No student named '{name}' found.")


def class_report(students):
    if not students:
        print("No students yet.")
        return

    scores = [s.score for s in students]           # comprehension
    passing = [s for s in students if s.score >= 50]  # comprehension

    average = sum(scores) / len(scores)
    print("\n--- Class Report ---")
    print(f"Total students: {len(students)}")
    print(f"Class average score: {average:.2f}")
    print(f"Passing: {len(passing)} / {len(students)}")
    print(f"Highest score: {max(scores)}")
    print(f"Lowest score: {min(scores)}")


def show_menu():
    print("\n=== Student Management System ===")
    print("1. Add student")
    print("2. View all students")
    print("3. Search student by name")
    print("4. Delete student")
    print("5. Class report (average, pass rate, etc.)")
    print("6. Exit")


def main():
    students = load_students()

    while True:
        show_menu()
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            delete_student(students)
        elif choice == "5":
            class_report(students)
        elif choice == "6":
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice — please enter a number from 1 to 6.")


if __name__ == "__main__":
    # This line means: "only run main() if this file is run directly,
    # not if it's imported as a module into another file." A common
    # professional pattern you'll see in almost every real Python project.
    main()
