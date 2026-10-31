# Mini Project — Task Tracker v5

Version 5 is a real menu program. It loops until the user quits, and uses decisions to react to each choice. It uses everything from Module 05.

## What it uses

| Idea | Lesson |
|---|---|
| `if` / `elif` / `else` for the menu, and `not` for checks | Lesson 01 |
| `while True`, `for` and `enumerate` | Lesson 02 |
| `break`, `continue` and the loop `else` | Lesson 03 |

Two lines use things you have not met yet: `lambda` and a generator inside `sum()` (Module 06 and Module 13). Treat them as magic for now.

## Run it

```bash
python task_tracker/v5_control_flow/task_tracker_v5.py
```

Example session:

```text
Welcome to Task Tracker

1) Add a task   2) Show tasks   3) Mark done   4) Quit
Choose: 1
Task title: record lesson 05
Priority (H, M or L): h
Added: Record Lesson 05
...
1) Add a task   2) Show tasks   3) Mark done   4) Quit
Choose: 2
1. [ ] Record Lesson 05     High
...
Choose: 4
Goodbye! 0 of 1 tasks done.
```

## Your turn

1. Add a menu option that removes a task.
2. Show only the tasks that are not done, with a new menu option.
3. Count how many tasks are High priority with a loop and an `if`.

## Next version

Module 06 adds functions, so v6 can split this big loop into small, named, reusable pieces.
