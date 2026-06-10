# Python Cheat Sheet

## Variables

### Syntax

```python
name = "Anusha"
age = 30
salary = 50000
```

### What it does

Stores data in memory.

### When to use

Whenever information needs to be reused later.

### Real Project Usage

Store user names, API keys, model settings, file paths.

---

## Data Types

| Type  | Example        | Use             |
| ----- | -------------- | --------------- |
| str   | "hello"        | Text            |
| int   | 10             | Whole numbers   |
| float | 10.5           | Decimal values  |
| bool  | True           | Yes/No logic    |
| list  | [1,2,3]        | Multiple items  |
| tuple | (1,2,3)        | Fixed values    |
| set   | {1,2,3}        | Unique values   |
| dict  | {"name":"Anu"} | Structured data |

---

## Input and Output

### Syntax

```python
name = input("Enter name: ")
print(name)
```

### What it does

Takes input from user and displays output.

---

## Operators

### Arithmetic

```python
+
-
*
/
/
//
%
**
```

### Example

```python
10 + 5
10 * 5
10 % 3
```

---

## Conditions

### Syntax

```python
if age >= 18:
    print("Adult")
else:
    print("Minor")
```

### What it does

Executes code based on conditions.

### Real Project Usage

Authentication, validation, decision making.

---

## Loops

### For Loop

```python
for i in range(5):
    print(i)
```

### While Loop

```python
count = 0

while count < 5:
    count += 1
```

### Use

Repeating tasks.

---

## Strings

### Common Methods

```python
text.lower()
text.upper()
text.title()
text.replace()
text.split()
text.strip()
```

### Example

```python
name = "anusha"

name.title()
```

Output:

```python
Anusha
```

### Real Project Usage

Data cleaning.

---

## Lists

### Syntax

```python
fruits = ["apple","banana","mango"]
```

### Common Methods

```python
append()
remove()
sort()
reverse()
len()
```

### Loop Through List

```python
for fruit in fruits:
    print(fruit)
```

### Real Project Usage

Store records, datasets, API results.

---

## Tuples

### Syntax

```python
coordinates = (10,20)
```

### What it does

Stores immutable values.

### Difference from List

Cannot modify after creation.

---

## Sets

### Syntax

```python
numbers = {1,2,3}
```

### What it does

Stores unique values only.

### Example

```python
{1,1,2,2,3}
```

Output:

```python
{1,2,3}
```

---

## Dictionaries

### Syntax

```python
employee = {
    "name":"Anu",
    "salary":50000
}
```

### Access Data

```python
employee["name"]
```

### Common Methods

```python
keys()
values()
items()
```

### Real Project Usage

JSON responses from APIs.

---

## Functions

### Syntax

```python
def greet(name):
    return f"Hello {name}"
```

### What it does

Reusable code block.

### Why Important

Large projects are built using functions.

---

## File Handling

### Read File

```python
with open("data.txt","r") as file:
    content = file.read()
```

### Write File

```python
with open("data.txt","w") as file:
    file.write("Hello")
```

### Real Project Usage

Logs, prompts, datasets.

---

## Exception Handling

### Syntax

```python
try:
    result = 10 / 0

except ZeroDivisionError:
    print("Cannot divide by zero")
```

### What it does

Prevents crashes.

---

## CSV Handling

### Read CSV

```python
import csv

with open("employees.csv") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
```

### Real Project Usage

Data processing.

---

## List Comprehension

### Syntax

```python
numbers = [1,2,3,4]

squares = [n*n for n in numbers]
```

### Output

```python
[1,4,9,16]
```

### Why Use

Cleaner than loops.

---

## Useful Built-in Functions

```python
len()
sum()
max()
min()
sorted()
type()
range()
```

### Examples

```python
len(numbers)

max(numbers)

sum(numbers)
```

---

## Common Errors

### IndexError

Cause:

```python
fruits[10]
```

Fix:

Check list length.

---

### KeyError

Cause:

```python
employee["city"]
```

Fix:

```python
employee.get("city")
```

---

### NameError

Cause:

Variable not defined.

Fix:

Create variable before using.

---

## Interview Questions

### List vs Tuple

List:

* Mutable

Tuple:

* Immutable

---

### Dictionary vs Set

Dictionary:

* Key-value pairs

Set:

* Unique values only

---

### Why Functions?

* Reusability
* Cleaner code
* Easier maintenance
