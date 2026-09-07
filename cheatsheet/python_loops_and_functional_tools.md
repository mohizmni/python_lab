# Python Collections, Loops & Functional Tools — Quick Cheat Sheet

> A compact Python reference for Lists, Tuples, Loops, Range, Enumerate, Zip, Comprehensions, Map, Filter, Sum, and Lambda.

---

# Lists

## Create

```python
items = [1, 2, 3]
mixed = [1, "Python", True, 3.14]
empty = []
```

## Convert

```python
list("abc")
# ['a', 'b', 'c']
```

## Access

```python
items[0]       # first item
items[-1]      # last item
items[-2]      # second-to-last item

len(items)     # number of items
2 in items     # membership → True / False
```

## Slicing

```python
items[start:stop]       # stop excluded
items[:3]               # first 3 items
items[2:]               # from index 2
items[:]                # shallow copy
items[::2]              # every 2nd item
items[::-1]             # reversed copy
```

## Modify

```python
items[0] = 10           # change item

del items[0]            # delete by index
del items[1:3]          # delete slice
```

## List Methods

```python
items.append(x)         # add ONE item
items.extend(iterable)  # add MULTIPLE items
items.insert(i, x)      # insert at index

items.remove(x)         # remove FIRST matching value

items.pop()             # remove + return LAST item
items.pop(i)            # remove + return item at index

items.clear()           # remove all items

items.sort()            # sort IN PLACE
items.sort(reverse=True)

items.reverse()         # reverse IN PLACE

items.index(x)          # index of FIRST match
```

## `append()` vs `extend()`

```python
items = [1, 2]

items.append([3, 4])
# [1, 2, [3, 4]]
```

```python
items = [1, 2]

items.extend([3, 4])
# [1, 2, 3, 4]
```

## `sort()` vs `sorted()`

```python
items.sort()                    # modifies original list

sorted(items)                   # returns NEW sorted list
sorted(items, reverse=True)
```

---

# Tuples

## Create

```python
items = (1, 2, 3)
empty = ()
single = (10,)            # comma required
```

## Convert

```python
tuple("abc")
# ('a', 'b', 'c')
```

## Access

```python
items[0]        # first item
items[-1]       # last item
items[-2]       # second-to-last item

len(items)      # number of items
2 in items      # membership → True / False
```

## Slicing

```python
items[start:stop]       # stop excluded
items[:3]
items[2:]
items[::-1]             # reversed tuple
```

## Immutable

```python
items[0] = 10
# TypeError
```

```python
del items[0]
# TypeError
```

> Tuples cannot be modified after creation.

## Tuple Methods

```python
items.count(x)          # number of occurrences
items.index(x)          # index of FIRST occurrence
```

## `sorted()` with Tuples

```python
numbers = (3, 1, 2)

sorted(numbers)
# [1, 2, 3]
```

> `sorted()` returns a new **List**, not a Tuple.

---

# Unpacking

## Basic Unpacking

```python
data = ["Alice", 25, "Python"]

name, age, language = data
```

## Star Unpacking

```python
name, *rest = data

# rest → [25, "Python"]
```

```python
first, *middle, last = [1, 2, 3, 4, 5]

# first  → 1
# middle → [2, 3, 4]
# last   → 5
```

> `*rest` always creates a List.

---

# Nested Lists

```python
data = [
    ["Alice", 25],
    ["Bob", 30]
]

data[0]       # ["Alice", 25]
data[0][1]    # 25
```

---

# Common Errors

```python
items[99]
# IndexError
```

```python
items.remove("x")
# ValueError if "x" does not exist
```

```python
items.index("x")
# ValueError if "x" does not exist
```

```python
a, b = [1, 2, 3]
# ValueError → unpacking mismatch
```

```python
tuple_data[0] = 10
# TypeError → tuple is immutable
```

---

# List vs Tuple

| Feature    | List | Tuple |
| ---------- | ---- | ----- |
| Syntax     | `[]` | `()`  |
| Mutable    | Yes  | No    |
| Ordered    | Yes  | Yes   |
| Indexing   | Yes  | Yes   |
| Slicing    | Yes  | Yes   |
| Duplicates | Yes  | Yes   |
| `append()` | Yes  | No    |
| `remove()` | Yes  | No    |
| `sort()`   | Yes  | No    |
| `count()`  | No   | Yes   |
| `index()`  | Yes  | Yes   |

---

# Loops

## `for`

```python
for item in iterable:
    print(item)
```

```python
for char in "Python":
    print(char)
```

## `while`

```python
while condition:
    # code
```

```python
count = 0

while count < 5:
    print(count)
    count += 1
```

## `break`

Stops the loop completely.

```python
for num in numbers:
    if num == 5:
        break
```

## `continue`

Skips the current iteration.

```python
for num in numbers:
    if num % 2 == 0:
        continue

    print(num)
```

## Nested Loops

```python
for i in range(3):
    for j in range(2):
        print(i, j)
```

## Loop `else`

Runs only if the loop finishes without `break`.

```python
for num in numbers:
    if num == 5:
        break
else:
    print("Not found")
```

```text
break       → stop loop
continue    → skip current iteration
else        → runs if no break occurs
```

---

# Range

## Syntax

```python
range(stop)
range(start, stop)
range(start, stop, step)
```

> `stop` is always excluded.

## Examples

```python
range(5)
# 0, 1, 2, 3, 4
```

```python
range(2, 6)
# 2, 3, 4, 5
```

```python
range(0, 10, 2)
# 0, 2, 4, 6, 8
```

```python
range(10, 0, -2)
# 10, 8, 6, 4, 2
```

## Common Patterns

```python
for i in range(5):
    print(i)
```

```python
for i in range(1, 11):
    print(i)
```

```python
for i in range(10, 0, -1):
    print(i)
```

## Convert to List

```python
list(range(5))
# [0, 1, 2, 3, 4]
```

## Important

```python
range()
# TypeError
```

```python
range(1.5, 5)
# TypeError
```

> `range()` uses integers.

---

# Enumerate

Adds an index while iterating.

## Syntax

```python
enumerate(iterable)
enumerate(iterable, start)
```

## Basic

```python
languages = ["Python", "Java", "C++"]

for index, language in enumerate(languages):
    print(index, language)
```

```text
0 Python
1 Java
2 C++
```

## Custom Start

```python
for index, language in enumerate(languages, start=1):
    print(index, language)
```

```text
1 Python
2 Java
3 C++
```

## Convert to List

```python
list(enumerate(languages))

# [(0, "Python"), (1, "Java"), (2, "C++")]
```

```text
enumerate() → index + value
start       → starting index
```

---

# Zip

Iterates over multiple iterables in parallel.

## Syntax

```python
zip(iterable1, iterable2, ...)
```

## Basic

```python
names = ["Alice", "Bob", "John"]
ages = [25, 30, 22]

for name, age in zip(names, ages):
    print(name, age)
```

## Convert to List

```python
list(zip(names, ages))

# [
#     ("Alice", 25),
#     ("Bob", 30),
#     ("John", 22)
# ]
```

## Multiple Iterables

```python
names = ["Alice", "Bob"]
ages = [25, 30]
jobs = ["Developer", "Designer"]

list(zip(names, ages, jobs))
```

```python
[
    ("Alice", 25, "Developer"),
    ("Bob", 30, "Designer")
]
```

> `zip()` stops when the shortest iterable is exhausted.

---

# List Comprehension

Creates a new List concisely.

## Basic Syntax

```python
[expression for item in iterable]
```

## Example

```python
numbers = [1, 2, 3, 4]

squares = [num ** 2 for num in numbers]

# [1, 4, 9, 16]
```

## With Condition

```python
[expression for item in iterable if condition]
```

```python
even = [num for num in numbers if num % 2 == 0]

# [2, 4]
```

## With `range()`

```python
even = [num for num in range(21) if num % 2 == 0]

# [0, 2, 4, ..., 20]
```

## `if / else`

```python
[
    value_if_true if condition else value_if_false
    for item in iterable
]
```

```python
result = [
    "even" if num % 2 == 0 else "odd"
    for num in range(5)
]

# ["even", "odd", "even", "odd", "even"]
```

## Nested Comprehension

```python
matrix = [[1, 2], [3, 4]]

flat = [num for row in matrix for num in row]

# [1, 2, 3, 4]
```

---

# Map

Applies a function to every item.

## Syntax

```python
map(function, iterable)
```

## Example

```python
numbers = [1, 2, 3, 4]

result = map(lambda x: x ** 2, numbers)

list(result)
# [1, 4, 9, 16]
```

## Named Function

```python
def square(x):
    return x ** 2

list(map(square, numbers))
```

## Multiple Iterables

```python
a = [1, 2, 3]
b = [10, 20, 30]

list(map(lambda x, y: x + y, a, b))

# [11, 22, 33]
```

```text
map() → TRANSFORM every item
```

---

# Filter

Keeps items where the function returns `True`.

## Syntax

```python
filter(function, iterable)
```

## Example

```python
numbers = [1, 2, 3, 4, 5, 6]

result = filter(lambda x: x % 2 == 0, numbers)

list(result)
# [2, 4, 6]
```

## Named Function

```python
def is_even(x):
    return x % 2 == 0

list(filter(is_even, numbers))
```

```text
filter() → SELECT matching items
```

---

# Map vs Filter

```text
map()       → TRANSFORM
filter()    → SELECT
```

```python
# map
list(map(lambda x: x * 2, [1, 2, 3]))
# [2, 4, 6]
```

```python
# filter
list(filter(lambda x: x > 1, [1, 2, 3]))
# [2, 3]
```

---

# Sum

Adds values together.

## Syntax

```python
sum(iterable)
sum(iterable, start)
```

## Examples

```python
sum([10, 20, 30])
# 60
```

```python
sum([10, 20, 30], start=100)
# 160
```

```python
sum([], start=10)
# 10
```

```python
sum(range(1, 6))
# 15
```

```text
sum(iterable, start=0) → TOTAL
```

---

# Lambda

Anonymous function for short expressions.

## Syntax

```python
lambda arguments: expression
```

## Examples

```python
square = lambda x: x ** 2

square(5)
# 25
```

```python
add = lambda a, b: a + b

add(2, 3)
# 5
```

## With `map()`

```python
list(map(lambda x: x ** 2, numbers))
```

## With `filter()`

```python
list(filter(lambda x: x % 2 == 0, numbers))
```

## With `sorted()`

```python
sorted(words, key=lambda x: len(x))
```

> Use `lambda` for small, simple functions. Prefer `def` for complex or reusable functions.

---

# Common Patterns

## Loop + Range

```python
for i in range(10):
    print(i)
```

## Loop + Enumerate

```python
for i, value in enumerate(items):
    print(i, value)
```

## Loop + Zip

```python
for name, age in zip(names, ages):
    print(name, age)
```

## List Comprehension

```python
[x ** 2 for x in numbers]
```

## Filter Comprehension

```python
[x for x in numbers if x > 10]
```

## Map

```python
list(map(lambda x: x * 2, numbers))
```

## Filter

```python
list(filter(lambda x: x > 10, numbers))
```

## Sum

```python
sum(numbers)
```

---

# Quick Reference

```text
LIST
[]                  → mutable collection
append(x)           → add ONE item
extend(x)           → add MANY items
insert(i, x)        → insert at index
remove(x)           → remove by VALUE
pop(i)              → remove by INDEX + return item
sort()              → sort IN PLACE
sorted(x)           → return NEW sorted list
reverse()           → reverse IN PLACE
index(x)            → find first index
len(x)              → number of items
```

```text
TUPLE
()                  → immutable collection
count(x)            → count occurrences
index(x)            → find first index
sorted(x)           → return NEW sorted list
```

```text
LOOPS
for                 → iterate
while               → repeat while condition is True
break               → stop loop
continue            → skip current iteration
else                → runs if no break occurs
```

```text
RANGE
range(stop)
range(start, stop)
range(start, stop, step)

stop                → always excluded
```

```text
ITERATION
enumerate()         → index + value
zip()               → multiple iterables in parallel
```

```text
FUNCTIONAL TOOLS
comprehension       → create a list concisely
map()               → TRANSFORM
filter()            → SELECT
sum()               → TOTAL
lambda              → small anonymous function
```

---

# Key Differences

```text
append() vs extend()

append()            → add ONE item
extend()            → add MULTIPLE items
```

```text
remove() vs pop()

remove(x)           → remove by VALUE
pop(i)              → remove by INDEX + return item
```

```text
sort() vs sorted()

sort()              → modifies original list
sorted()            → returns a NEW sorted list
```

```text
for vs while

for                 → iterate over an iterable
while               → repeat while condition is True
```

```text
break vs continue

break               → exit the loop
continue            → skip current iteration
```

```text
enumerate() vs zip()

enumerate()         → index + value
zip()               → multiple iterables together
```

```text
map() vs filter()

map()               → TRANSFORM values
filter()            → SELECT values
```

---

# Error Quick Reference

| Error        | Common Cause                       |
| ------------ | ---------------------------------- |
| `IndexError` | Index is out of range              |
| `ValueError` | Invalid value / unpacking mismatch |
| `TypeError`  | Wrong type / modifying a tuple     |

---

# One-Line Memory

```text
range()       → COUNT
enumerate()   → INDEX
zip()         → PAIR
for           → ITERATE
while         → REPEAT
break         → STOP
continue      → SKIP
comprehension → CREATE
map()         → TRANSFORM
filter()      → SELECT
sum()         → TOTAL
lambda        → FUNCTION
```
