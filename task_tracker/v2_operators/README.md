# Mini Project — Task Tracker v2

Version 2 of the project that grows through the whole series. Version 1 (Module 01) saved one task. Version 2 adds maths, comparisons and logic.

## What it uses

| Idea | Lesson |
|---|---|
| `-`, `/`, `*` and `round()` | Lesson 01 |
| `>`, `!=` and the constant `MAX_TASKS` | Lesson 01 |
| `and`, `in`, and truthy values | Lesson 02 |

## Run it

```bash
python task_tracker/v2_operators/task_tracker_v2.py
```

Example session:

```text
Welcome to Task Tracker v2
Tasks done today: 3
Tasks planned today: 8
Top priority (high, medium, low): low
Tasks left: 5
Progress: 38 %
Too many tasks. Move one to tomorrow.
```

## Your turn

1. Add a rule: if all tasks are done (`tasks_left == 0`), print a congratulation message.
2. Change `MAX_TASKS` to 3 and run it again. Which lines change?
3. Use `not` to print a warning when `valid_priority` is `False`.

## Next version

Module 03 adds strings, so v3 can clean the text that the user types.
