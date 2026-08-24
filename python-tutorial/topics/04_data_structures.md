# 04 — Data Structures (from absolute zero)

## 1. Real-life analogy

- **List** = a shopping list on paper — items in order, you can cross one
  out, add new ones, and the same item can appear twice.
- **Tuple** = your birth date (day, month, year) — fixed, it will never
  change, ever.
- **Dictionary** = a real dictionary book — you look up a WORD (key) to
  find its MEANING (value). No two identical words; each has one meaning.
- **Set** = a jar of unique marbles — no duplicates allowed, and you don't
  care about their order, just which colors exist.

## 2. Lists — ordered, changeable collections

```python
fruits = ["apple", "banana", "mango"]

print(fruits[0])      # 'apple'  -> same indexing rules as strings!
print(fruits[-1])     # 'mango'  -> last item
print(len(fruits))    # 3        -> how many items

# Adding items
fruits.append("orange")          # adds to the END
print(fruits)   # ['apple', 'banana', 'mango', 'orange']

fruits.insert(1, "grape")        # insert at a SPECIFIC position
print(fruits)   # ['apple', 'grape', 'banana', 'mango', 'orange']

# Removing items
fruits.remove("banana")          # removes by VALUE (the actual item)
print(fruits)

popped = fruits.pop()            # removes and returns the LAST item
print(popped)
print(fruits)

# Changing an item
fruits[0] = "kiwi"
print(fruits)

# Checking if something exists
print("mango" in fruits)   # True or False

# Looping through every item
for fruit in fruits:
    print("I like", fruit)
```

**Trace it step by step:** Start with `["apple", "banana", "mango"]`.
`.append("orange")` puts orange at the end → 4 items now. `.insert(1,
"grape")` shoves "grape" into position 1, shifting banana/mango/orange one
step right.

## 3. Tuples — ordered, but LOCKED (immutable)

```python
coordinates = (10, 20)     # round brackets = tuple

print(coordinates[0])     # 10
# coordinates[0] = 5      # ❌ TypeError: tuples don't support item assignment
```

**Why use a tuple instead of a list at all?** When you want to GUARANTEE
the data never accidentally changes — like GPS coordinates, RGB colors
`(255, 0, 0)`, or a date `(2024, 1, 15)`. Locking it prevents bugs.

## 4. Dictionaries — key → value lookups

```python
student = {
    "name": "Asha",
    "age": 25,
    "course": "Python"
}

print(student["name"])     # 'Asha'  -> look up value using its key
print(student.get("age"))  # 25      -> .get() is a safer way to look up

# Updating and adding
student["age"] = 26                 # update existing key
student["grade"] = "A"              # add a brand new key
print(student)

# Removing a key
del student["grade"]
print(student)

# Checking if a key exists
print("name" in student)    # True

# Looping through a dictionary
for key, value in student.items():
    print(key, "->", value)
```

**Why `.get()` is safer than `[]`:**
```python
print(student["email"])       # ❌ KeyError: 'email' -> crashes! key doesn't exist
print(student.get("email"))   # None -> just gives "nothing found", no crash
print(student.get("email", "N/A"))  # 'N/A' -> gives a DEFAULT value instead
```

## 5. Sets — unique values only, order doesn't matter

```python
tags = {"python", "coding", "python", "beginner"}
print(tags)   # {'python', 'coding', 'beginner'} -> duplicate "python" auto-removed!

tags.add("tutorial")
print(tags)

# Very useful trick: instantly remove duplicates from a list
numbers = [1, 2, 2, 3, 3, 3, 4]
unique_numbers = set(numbers)
print(unique_numbers)   # {1, 2, 3, 4}
print(list(unique_numbers))   # back to a list: [1, 2, 3, 4]
```

## 6. Nesting — putting structures inside each other (this is HUGE in real projects)

```python
# A list of dictionaries -> very common real-world pattern!
students = [
    {"name": "Asha", "score": 88},
    {"name": "Ravi", "score": 92},
    {"name": "Meena", "score": 79}
]

for student in students:
    print(f"{student['name']} scored {student['score']}")

# Accessing nested data
print(students[0]["name"])   # 'Asha' -> first student's name
```

## 7. Which one should I use? (decision logic)

Ask yourself these questions in order:
1. "Do I need key-value pairs (labeled data)?" → **dictionary**
2. "Do I need to guarantee it NEVER changes?" → **tuple**
3. "Do I care about duplicates being removed / don't care about order?" → **set**
4. "None of the above, just a general ordered collection I can edit?" → **list** (most common choice)

## 8. Common mistakes

```python
fruits = ["apple", "banana"]
print(fruits[5])   # ❌ IndexError: list index out of range
```

```python
student = {"name": "Asha"}
print(student["Name"])   # ❌ KeyError -> keys are case-sensitive! "Name" != "name"
```

## 9. Practice

1. Create a list of 5 favorite movies. Add a 6th, remove one, print the
   final list.
2. Create a dictionary for a "product" with keys `name`, `price`, `stock`.
   Print a sentence using all 3 values with an f-string.
3. Create a list of 3 dictionaries representing 3 friends (`name`, `age`).
   Loop through and print `"<name> is <age> years old"` for each.
4. Take the list `[5, 1, 5, 2, 3, 1, 4]` and print only the unique values
   using a set.

---
⬅ [Previous: Strings](03_strings.md) | ➡ [Next: Control Flow](05_control_flow.md)
