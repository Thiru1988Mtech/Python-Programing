# 11 — NumPy (from absolute zero)

## 1. Real-life analogy

Imagine you have 1,000 sticky notes with numbers, and you want to add 5 to
EVERY single note. Doing it by hand (one sticky note at a time) is slow.
NumPy is like a **magic stamp** that applies "+5" to all 1,000 notes at
once, instantly.

## 2. Why not just use a normal Python list?

```python
prices = [10, 20, 30]
# prices + 5   -> ❌ TypeError! You cannot add a number to a whole list directly
```
With a normal list, you'd need a loop or comprehension to touch every
item. NumPy arrays let you skip the loop entirely.

## 3. Setup

```bash
pip install numpy
```

## 4. Creating your first array

```python
import numpy as np    # 'np' is just a shorter nickname, used everywhere by convention

arr = np.array([1, 2, 3, 4, 5])
print(arr)          # [1 2 3 4 5]
print(type(arr))    # <class 'numpy.ndarray'>
```

## 5. Doing math on the WHOLE array at once (the main superpower)

```python
arr = np.array([1, 2, 3, 4, 5])

print(arr + 5)     # [ 6  7  8  9 10]  -> adds 5 to EVERY element
print(arr * 2)     # [ 2  4  6  8 10]  -> multiplies EVERY element by 2
print(arr ** 2)    # [ 1  4  9 16 25]  -> squares EVERY element
print(arr > 2)     # [False False  True  True  True] -> compares EVERY element
```
No loop needed — NumPy applies the operation to every single item
automatically. This is called "vectorization."

## 6. Built-in statistics — instant answers about your data

```python
arr = np.array([10, 20, 30, 40, 50])

print(arr.sum())     # 150  -> total of all values
print(arr.mean())    # 30.0 -> average
print(arr.max())     # 50   -> largest value
print(arr.min())     # 10   -> smallest value
print(arr.std())     # standard deviation -> how spread out the values are
```

## 7. 2D arrays — grids of numbers (like a mini spreadsheet)

```python
matrix = np.array([[1, 2, 3],
                    [4, 5, 6]])

print(matrix.shape)   # (2, 3) -> 2 rows, 3 columns
print(matrix[0])      # [1 2 3]  -> the whole first row
print(matrix[1, 2])   # 6        -> row index 1, column index 2
print(matrix[:, 0])   # [1 4]    -> ALL rows, only column 0
```
Reading `matrix[1, 2]`: "go to row 1 (the second row), then column 2 (the
third value in that row)" → `6`.

## 8. Filtering with conditions (boolean indexing) — very powerful

```python
data = np.array([10, 25, 3, 47, 8])

mask = data > 10          # [False  True False  True False]
print(mask)

filtered = data[data > 10]   # only keeps values where the condition is True
print(filtered)               # [25 47]
```
Read as: *"Give me only the values from `data` where the value is greater
than 10."* No loop, no if-statement needed — NumPy does the filtering for
you in one line.

## 9. Generating arrays quickly

```python
print(np.arange(0, 10, 2))    # [0 2 4 6 8]   -> like range(), but as an array
print(np.zeros(3))             # [0. 0. 0.]    -> array of 3 zeros
print(np.ones((2, 2)))         # 2x2 grid of 1s
print(np.linspace(0, 1, 5))    # 5 evenly spaced numbers between 0 and 1
```

## 10. Full worked example — analyzing test scores

```python
import numpy as np

scores = np.array([88, 92, 79, 95, 60, 45, 73])

print("Average score:", scores.mean())
print("Highest score:", scores.max())
print("Lowest score:", scores.min())

passing_scores = scores[scores >= 60]
print("Passing scores:", passing_scores)
print("Number passing:", len(passing_scores))

# Add 5 bonus marks to everyone
adjusted_scores = scores + 5
print("Adjusted scores:", adjusted_scores)
```

## 11. Common mistakes

```python
arr = np.array([1, 2, "three"])   # ⚠️ mixing types converts EVERYTHING to text!
print(arr)                         # ['1' '2' 'three'] -> now math won't work as expected
```
Keep arrays consistent — all numbers, or all text, not mixed.

## 12. Practice

1. Create an array of numbers 1–10, print only the ones greater than 5.
2. Create a 3x3 matrix and print its `.shape` and the value at row 2,
   column 1.
3. Create an array of your last 5 test scores and print `.mean()` and
   `.max()`.
4. Given `temps = np.array([20, 35, 15, 40, 25])`, filter to only values
   above 30.

---
⬅ [Previous: Comprehensions](10_comprehensions.md) | ➡ [Next: Pandas](12_pandas.md)
