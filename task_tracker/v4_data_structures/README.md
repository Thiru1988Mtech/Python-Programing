# Mini Project — Task Tracker v4

Version 4 keeps **many** tasks. Each task is a dictionary, and all tasks live in a list. It uses everything from Module 04.

## What it uses

| Idea | Lesson |
|---|---|
| List of tasks, `.append()`, `.sort(key=...)` | Lesson 01 |
| Dictionaries for each task, a set of tags, `PRIORITY_NAMES[...]` | Lesson 02 |
| `copy.deepcopy()` for a backup, unpacking with `*others` | Lesson 03 |

Two lines use things you have not met yet: the `for` loop (Module 05) and `lambda` (Module 06). Treat them as magic for now. They will make sense soon.

## Run it

```bash
python task_tracker/v4_data_structures/task_tracker_v4.py
```

Example session:

```text
Welcome to Task Tracker
New task title: pay bills
Priority (H, M or L): h
Record Lesson 04     High     ['python', 'video']
Pay Bills            High     []
Upload Video         Medium   ['video']
Write Notes          Low      ['python']
Next up: Record Lesson 04 (and 3 more)
Before sorting, the first task was: Record Lesson 04
```

## Your turn

1. Add a fourth starting task with two tags.
2. Print how many tasks have the tag `python`. (Hint: `"python" in task["tags"]`.)
3. Change the sort so the titles are in alphabetical order inside each priority.

## Next version

Module 05 adds decisions and loops, so v5 can show a menu and keep asking for tasks.
