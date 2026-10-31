# Task Tracker v1 - Module 01 mini project
APP_NAME = "Task Tracker"        # constant by convention

print("Welcome to", APP_NAME)
title = input("Task title: ")
priority_text = input("Priority (1 = high, 3 = low): ")
priority = int(priority_text)    # input() always returns text

if title:                        # empty text is falsy
    print("Saved task:", title, "| priority:", priority)
else:
    print("No task entered.")
