# Task Tracker v2 - Module 02 mini project
APP_NAME = "Task Tracker"
MAX_TASKS = 5                    # constant by convention

print("Welcome to", APP_NAME, "v2")
tasks_done = int(input("Tasks done today: "))
tasks_total = int(input("Tasks planned today: "))
priority = input("Top priority (high, medium, low): ")

tasks_left = tasks_total - tasks_done                  # arithmetic
valid_priority = priority in ["high", "medium", "low"]  # membership
too_many = tasks_total > MAX_TASKS                     # comparison

print("Tasks left:", tasks_left)
if tasks_total and valid_priority:                     # zero is falsy
    percent = tasks_done / tasks_total * 100
    print("Progress:", round(percent), "%")
else:
    print("Please enter at least one task and a valid priority.")
if too_many and priority != "high":                    # logic
    print("Too many tasks. Move one to tomorrow.")
