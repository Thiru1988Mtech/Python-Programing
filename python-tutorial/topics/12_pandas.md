# 12 — Pandas (from absolute zero)

## 1. Real-life analogy

Pandas turns Python into Excel. A **DataFrame** is a spreadsheet: rows are
records (like "one student"), columns are fields (like "Name", "Age",
"Score"). A **Series** is just ONE column of that spreadsheet by itself.

## 2. Setup

```bash
pip install pandas
```

## 3. Creating your first DataFrame

```python
import pandas as pd    # 'pd' is the standard nickname, used everywhere

data = {
    "Name": ["Asha", "Ravi", "Meena", "Karan"],
    "Age": [25, 22, 28, 24],
    "Score": [88, 92, 79, 95]
}
df = pd.DataFrame(data)
print(df)
```
Output:
```
    Name  Age  Score
0   Asha   25     88
1   Ravi   22     92
2  Meena   28     79
3  Karan   24     95
```
Notice: each key in the dictionary became a COLUMN, and each list's items
became the ROWS under that column, matched by position.

## 4. Exploring a DataFrame — your first "get to know the data" toolkit

```python
print(df.head())       # shows the first 5 rows (all 4 here, since we only have 4)
print(df.shape)         # (4, 3) -> 4 rows, 3 columns
print(df.columns)       # Index(['Name', 'Age', 'Score'], dtype='object')
print(df.info())        # column types + how many non-empty values in each
print(df.describe())    # quick stats: mean, min, max, etc. (only for number columns)
```

## 5. Selecting columns and rows

```python
print(df["Name"])         # selects the 'Name' column -> a Series (single column)
print(df[["Name", "Age"]]) # selects MULTIPLE columns -> pass a list of names

print(df.loc[0])          # selects row at label/index 0 (the first row)
print(df.iloc[0])         # selects row at POSITION 0 (same result here)
```

## 6. Filtering rows — asking questions about your data

```python
print(df[df["Score"] > 85])
```
Read as: *"Give me all rows where the Score column value is greater than
85."*

**Trace it:** `df["Score"] > 85` first creates a True/False list for every
row (like NumPy's boolean filtering). Then `df[...]` uses that list to
keep only the `True` rows.

**Combining multiple conditions:**
```python
print(df[(df["Score"] > 80) & (df["Age"] < 26)])
# Use & for AND, | for OR -- and always wrap each condition in ( )
```

## 7. Adding and modifying columns

```python
df["Passed"] = df["Score"] >= 80    # creates a new column instantly
print(df)

df["Grade"] = df["Score"].apply(lambda s: "A" if s >= 90 else "B" if s >= 75 else "C")
print(df)
```

## 8. Sorting

```python
print(df.sort_values("Score", ascending=False))   # highest score first
```

## 9. Grouping and aggregating — answering "on average, per group..."

```python
print(df.groupby("Passed")["Score"].mean())
```
Read as: *"Split the rows into groups based on Passed (True/False), then
find the average Score within each group."*

## 10. Reading and writing real files

```python
df = pd.read_csv("students.csv")        # load data from a real CSV file
df.to_csv("output.csv", index=False)    # save your DataFrame back to a CSV
```

## 11. Full worked example — analyzing a small sales dataset

```python
import pandas as pd

data = {
    "Product": ["Pen", "Notebook", "Bag", "Pencil", "Eraser"],
    "Price": [10, 40, 500, 5, 3],
    "Quantity_Sold": [100, 60, 15, 200, 150]
}
df = pd.DataFrame(data)

df["Revenue"] = df["Price"] * df["Quantity_Sold"]
print(df)

print("Total revenue:", df["Revenue"].sum())
print("Best-selling product:", df.loc[df["Quantity_Sold"].idxmax(), "Product"])

top_products = df.sort_values("Revenue", ascending=False)
print(top_products)
```

## 12. Common mistakes

```python
df["name"]   # ❌ KeyError if the actual column is "Name" -> column names are case-sensitive
```

```python
df[df.Score > 85]   # this ALSO works (attribute-style access) but is riskier
                     # if a column name has spaces or matches a method name
```

## 13. Practice

1. Create a DataFrame of 5 products with `Product`, `Price`, `Stock`.
2. Filter to show only products with `Price > 100`.
3. Add a column `Total_Value` = `Price * Stock`.
4. Sort by `Total_Value` descending and print the top row using `.iloc[0]`.

---
⬅ [Previous: NumPy](11_numpy.md) | ➡ [Next: Advanced Python](13_advanced_python.md)
