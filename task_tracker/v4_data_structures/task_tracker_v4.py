# Task Tracker v4 - Module 04 mini project
import copy

APP_NAME = "Task Tracker"
PRIORITY_NAMES = {"H": "High", "M": "Medium", "L": "Low"}   # dictionary lookup
ORDER = {"H": 1, "M": 2, "L": 3}                            # for sorting

# Each task is a dictionary. All tasks live in a list.
tasks = [
    {"title": "Record Lesson 04", "priority": "H", "tags": {"video", "python"}},
    {"title": "Write Notes", "priority": "L", "tags": {"python"}},
    {"title": "Upload Video", "priority": "M", "tags": {"video"}},
]

print("Welcome to", APP_NAME)
title = input("New task title: ").strip().title()
priority = input("Priority (H, M or L): ").strip().upper()

if title and priority in PRIORITY_NAMES:
    tasks.append({"title": title, "priority": priority, "tags": set()})

backup = copy.deepcopy(tasks)                      # safe copy of nested data
tasks.sort(key=lambda task: ORDER[task["priority"]])   # high priority first

for task in tasks:
    name = PRIORITY_NAMES[task["priority"]]
    print(f"{task['title']:<20} {name:<8} {sorted(task['tags'])}")

first, *others = tasks                             # unpacking
print(f"Next up: {first['title']} (and {len(others)} more)")
print(f"Before sorting, the first task was: {backup[0]['title']}")
