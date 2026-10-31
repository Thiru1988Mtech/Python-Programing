# Mini Project — Task Tracker v3

Version 3 cleans and formats what the user types. It uses everything from Module 03.

## What it uses

| Idea | Lesson |
|---|---|
| Slicing, `len()` to shorten long titles | Lesson 01 |
| `.strip()`, `.upper()`, `.title()` and f-strings with alignment | Lesson 02 |
| Input and `in` from Modules 01 and 02 | Modules 01 to 02 |

## Run it

```bash
python task_tracker/v3_strings/task_tracker_v3.py
```

Example session:

```text
Welcome to Task Tracker
Task title:    record lesson 04
Priority (H, M or L): h
[H] Record Lesson 04     (16 characters)
```

## Your turn

1. Change `MAX_TITLE` to 12 and run it with a long title.
2. Print the first word of the title using `split()`.
3. Add a line that prints the title in capitals inside a box of `*` characters, using `"*" * width`.

## Next version

Module 04 adds lists and dictionaries, so v4 can keep many tasks at once.
