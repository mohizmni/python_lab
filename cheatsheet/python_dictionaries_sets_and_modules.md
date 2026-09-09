# Python Dictionaries, Sets & Modules — Quick Cheat Sheet

## Dictionaries

```text
dict                  → key/value pairs
dict[key]             → access value
get()                 → safe access
keys()                → keys
values()              → values
items()               → key + value
pop()                 → remove by key
popitem()             → remove last item
clear()               → remove everything
update()              → add/update multiple pairs
```

### Looping

```text
dictionary            → keys
dictionary.keys()     → keys
dictionary.values()   → values
dictionary.items()    → key + value

enumerate(...)        → add counter
enumerate(..., 1)     → counter starts at 1
```

### Examples

```python
products = {
    "Laptop": 990,
    "Phone": 600
}

products["Laptop"]                 # access
products.get("Laptop")             # safe access

for product in products:
    print(product)                 # keys

for price in products.values():
    print(price)                   # values

for product, price in products.items():
    print(product, price)          # key + value

for index, product in enumerate(products, 1):
    print(index, product)          # counter + key
```

---

## Sets

```text
Set          → unique values
add()        → add element
remove()     → remove; error if missing
discard()    → remove; no error if missing
clear()      → remove everything
```

### Set Operations

```text
|            → union
&            → intersection
-            → difference
^            → symmetric difference
in           → membership check
```

### Set Comparisons

```text
issubset()   → check subset
issuperset() → check superset
isdisjoint() → check no common elements
```

### Examples

```python
A = {1, 2, 3, 4, 5}
B = {2, 3, 4, 6}

A | B        # {1, 2, 3, 4, 5, 6}
A & B        # {2, 3, 4}
A - B        # {1, 5}
A ^ B        # {1, 5, 6}

5 in A       # True
```

---

## Modules & Imports

### Standard Library

```text
math         → mathematical operations
random       → random numbers
datetime     → dates and times
re           → regular expressions
```

### Import Syntax

```python
import math
```

→ Import the entire module.

```python
import math as m
```

→ Import module with an alias.

```python
from math import sqrt
```

→ Import only `sqrt`.

```python
from math import sqrt, pi
```

→ Import multiple items.

```python
from math import sqrt as s
```

→ Import `sqrt` with an alias.

```python
from math import *
```

→ Import everything; generally not recommended.

### Module Access

```python
import math

math.sqrt(36)
math.pi
```

```text
module.function()   → access a function
module.constant     → access a constant
```

---

## `if __name__ == "__main__"`

```python
if __name__ == "__main__":
    print("Running directly")
```

```text
Run file directly
→ __name__ == "__main__"
→ block runs

Import file as a module
→ __name__ != "__main__"
→ block does not run
```

---

## Quick Memory Guide

```text
DICTIONARY
key → value

SET
unique + unordered

LOOPS
keys()   → keys
values() → values
items()  → key + value

ENUMERATE
enumerate() → add counter

SET OPERATORS
| → union
& → common
- → difference
^ → not both

IMPORTS
import → module
from   → specific item
as     → alias

MAIN CHECK
if __name__ == "__main__":
```

## One-Line Memory

```text
dict → KEY/VALUE
keys → KEYS
values → VALUES
items → BOTH
get → SAFE ACCESS
pop → REMOVE
update → ADD/UPDATE

set → UNIQUE
add → ADD
remove → REMOVE + ERROR IF MISSING
discard → REMOVE + NO ERROR
| → UNION
& → COMMON
- → DIFFERENCE
^ → NOT BOTH

import → MODULE
from → SPECIFIC ITEM
as → ALIAS
```
