# Python: Basics to Production

One repository for the whole YouTube series **Python: Basics to Production**, from first program to production-level code. Each module is a folder. New modules are added as the series grows.

## Modules

| # | Module | Lessons | Task Tracker step |
|---|---|---|---|
| 01 | [Python Basics](module_01_basics/) | 3 | [v1_basics](task_tracker/v1_basics/) |
| 02 | [Operators](module_02_operators/) | 2 | [v2_operators](task_tracker/v2_operators/) |
| 03 | [Strings](module_03_strings/) | 2 | [v3_strings](task_tracker/v3_strings/) |
| 04 | [Data Structures](module_04_data_structures/) | 3 | [v4_data_structures](task_tracker/v4_data_structures/) |
| 05 | [Control Flow](module_05_control_flow/) | 3 | [v5_control_flow](task_tracker/v5_control_flow/) |

Planned: Functions, OOP, File & Data Handling, Exception Handling, Comprehensions, NumPy, Pandas, Advanced Python.

Each lesson folder has `slides/` (PowerPoint), `scripts/` (recording script), and `notebooks/` (a recording notebook with empty code cells, and an answer key with the code filled in and output saved).

## How to run

**Python version:** 3.12 is recommended. 3.11 is the minimum. These modules use the standard library only, so apart from Jupyter there is nothing else to install.

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook
```

Open a module folder, then a lesson folder, then `notebooks/`, and start with `L0X_recording.ipynb`.

## The Task Tracker project

A small app that grows with the series. Each step is a folder in [`task_tracker/`](task_tracker/) and uses only what you have learned so far.

| Step | Built in |
|---|---|
| v1_basics | Module 01 |
| v2_operators | Module 02 |
| v3_strings | Module 03 |
| v4_data_structures | Module 04 |
| v5_control_flow | Module 05 |

Run a step from the repository root, for example `python task_tracker/v1_basics/task_tracker_v1.py`.

## Folder layout

```text
python-basics-to-production/
├── README.md
├── requirements.txt
├── .gitignore
├── module_01_basics/
│   ├── README.md
│   └── lesson_01_.../
│       ├── README.md
│       ├── slides/
│       ├── scripts/
│       └── notebooks/
├── module_02_operators/
├── ...
└── task_tracker/
    ├── README.md
    └── v1_basics/
```

## Author

Thirumurugan Munusamy · YouTube: [@ThiruPhDAIResearchScientist](https://www.youtube.com/@ThiruPhDAIResearchScientist) · GitHub: [Thiru1988Mtech](https://github.com/Thiru1988Mtech)
