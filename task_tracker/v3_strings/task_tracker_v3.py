# Task Tracker v3 - Module 03 mini project
APP_NAME = "Task Tracker"
MAX_TITLE = 20                       # longest title we show

print("Welcome to", APP_NAME)
title = input("Task title: ").strip()          # remove stray spaces
priority_text = input("Priority (H, M or L): ").strip().upper()

if title and priority_text in ("H", "M", "L"):
    title = title.title()                      # Record lesson -> Record Lesson
    if len(title) > MAX_TITLE:                 # cut long titles with a slice
        shown = title[:MAX_TITLE - 3] + "..."
    else:
        shown = title
    print(f"[{priority_text}] {shown:<{MAX_TITLE}} ({len(title)} characters)")
else:
    print("Please enter a title and a priority of H, M or L.")
