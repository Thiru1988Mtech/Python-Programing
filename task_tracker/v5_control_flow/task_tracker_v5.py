# Task Tracker v5 - Module 05 mini project
APP_NAME = "Task Tracker"
PRIORITY_NAMES = {"H": "High", "M": "Medium", "L": "Low"}
ORDER = {"H": 1, "M": 2, "L": 3}
MAX_TITLE = 20

tasks = []                       # each task is a dictionary

print("Welcome to", APP_NAME)

while True:                      # the menu loop: runs until the user quits
    print()
    print("1) Add a task   2) Show tasks   3) Mark done   4) Quit")
    choice = input("Choose: ").strip()

    if choice == "1":
        title = input("Task title: ").strip().title()
        priority = input("Priority (H, M or L): ").strip().upper()
        if not title or priority not in PRIORITY_NAMES:
            print("Please enter a title and a priority of H, M or L.")
            continue             # back to the menu
        tasks.append({"title": title, "priority": priority, "done": False})
        print(f"Added: {title}")
    elif choice == "2":
        if not tasks:
            print("No tasks yet.")
        else:
            ordered = sorted(tasks, key=lambda task: ORDER[task["priority"]])
            for number, task in enumerate(ordered, start=1):
                mark = "x" if task["done"] else " "
                shown = task["title"]
                if len(shown) > MAX_TITLE:
                    shown = shown[:MAX_TITLE - 3] + "..."
                print(f"{number}. [{mark}] {shown:<{MAX_TITLE}} {PRIORITY_NAMES[task['priority']]}")
    elif choice == "3":
        title = input("Title to mark done: ").strip().title()
        for task in tasks:
            if task["title"] == title:
                task["done"] = True
                print(f"Done: {title}")
                break
        else:                    # no break: the title was not found
            print("Task not found.")
    elif choice == "4":
        break                    # leave the menu loop
    else:
        print("Please choose 1, 2, 3 or 4.")

done_count = sum(1 for task in tasks if task["done"])
print(f"Goodbye! {done_count} of {len(tasks)} tasks done.")
