# 08 — File & Data Handling (from absolute zero)

## 1. Real-life analogy

Everything your program stores in variables disappears the instant the
program stops running — like writing on a whiteboard that gets erased when
you leave the room. A **file** is like writing in a notebook instead —
it's still there when you come back.

## 2. Opening, writing, and closing a file — the safe pattern

```python
with open("notes.txt", "w") as file:    # "w" = write mode (creates or OVERWRITES the file)
    file.write("Learning Python is fun!\n")   # \n means "new line"
    file.write("This is my second line.\n")
```
Read this as: *"Open (or create) a file called notes.txt, in WRITE mode,
call it 'file' while we work with it. When we're done (end of the
indented block), close it automatically."*

The `with` keyword automatically closes the file for you, even if
something goes wrong — this prevents a common bug where forgetting to
close a file corrupts your data.

## 3. Reading a file back

```python
with open("notes.txt", "r") as file:   # "r" = read mode
    content = file.read()
    print(content)
```

**Reading line-by-line (very common for processing data):**
```python
with open("notes.txt", "r") as file:
    for line in file:
        print("Line:", line.strip())    # .strip() removes the trailing \n
```

## 4. The three file modes you'll use 90% of the time

| Mode | Meaning | What happens to existing content |
|------|---------|-----------------------------------|
| `"w"` | write | ⚠️ ERASES everything and starts fresh |
| `"a"` | append | keeps old content, adds new at the END |
| `"r"` | read | just reads, doesn't change anything |

```python
with open("notes.txt", "a") as file:
    file.write("Adding a new line without erasing old ones.\n")
```

## 5. Working with CSV files (spreadsheet-style data)

CSV = "Comma-Separated Values" — literally a plain text file where commas
separate columns, like a simple spreadsheet.

```python
import csv

# Writing a CSV (like creating a spreadsheet)
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "Grade"])   # this becomes the header row
    writer.writerow(["Asha", 25, "A"])
    writer.writerow(["Ravi", 22, "B"])

# Reading a CSV back
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)     # each row comes back as a LIST: ['Asha', '25', 'A']
```

## 6. Working with JSON (the format used by almost every website/API)

JSON looks just like a Python dictionary — that's not a coincidence, it's
designed to map directly onto one.

```python
import json

data = {"name": "Asha", "age": 25, "skills": ["Python", "SQL"]}

# Save a dictionary to a JSON file
with open("data.json", "w") as file:
    json.dump(data, file)

# Load it back as a dictionary
with open("data.json", "r") as file:
    loaded_data = json.load(file)
    print(loaded_data)
    print(loaded_data["name"])   # Asha
```

## 7. Full worked example — a simple contact saver

```python
import json

def save_contact(name, phone):
    try:
        with open("contacts.json", "r") as file:
            contacts = json.load(file)
    except FileNotFoundError:
        contacts = {}     # file doesn't exist yet -> start with an empty dict

    contacts[name] = phone

    with open("contacts.json", "w") as file:
        json.dump(contacts, file)

    print(f"Saved {name}'s contact!")

save_contact("Asha", "9876543210")
save_contact("Ravi", "9123456780")
```

## 8. Common mistakes

```python
with open("notes.txt", "w") as file:   # ⚠️ if the file already had important data,
    file.write("New content")          # this ERASES it completely! Use "a" if unsure.
```

```python
file = open("data.txt", "r")
print(file.read())
# forgot file.close()   -> may cause issues; always prefer 'with' instead
```

## 9. Practice

1. Write a `diary.txt` with 3 lines about your day, then read and print it
   back.
2. Create a CSV `fruits.csv` with columns `Fruit, Color` and 3 rows.
3. Save a dictionary about yourself as `profile.json`, load it back, and
   print your name from it.
4. Extend the `save_contact` example with a `load_contacts()` function that
   prints every saved contact.

---
⬅ [Previous: OOP](07_oop.md) | ➡ [Next: Exception Handling](09_exception_handling.md)
