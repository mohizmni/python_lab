# pyhton cheat sheet

## 1. python vs C++
### Variables declartion
c++:
int age = 21;
python:
# No explicit type declartion, python is dynamically typed
age = 21

### Comment 
c++: 
// comment 
Python:
# comment

## Data Types

### 1. Boolean - bool
True / False 
C++:
bool x = True;
Python: 
x = True

### 2. Integer - int
x = 10 
y = -5

### 3. Float - float
C++:
float x = 3.14f;
double x = 3.14;
Python: 
x = 3.14

### 4. String - str
Python: name = 'Mohadese' / "mohadese"
C++: string name = "mohadese";

### 5. List - list
Python: numbers = [10, 'hello', 3.14]
C++: vector<int> numbers = {1, 2, 3};

### 6. Tuple - tuple
Python: point = (10, 20, 'hi')
C++: -

### 7. Set - set
Python: numbers = {1, 'hi', 3}

### 8. Dictionary
Python:
person = {
    "name": "mohi"
    "age": 21
}
person["name"]
C++:
std::map<string, ...>

### 9. Range
Python: range(5) // 0 , 1 ,2 ,3 ,4 
range(start, stop, step) // range(1, 10, 2) = 1,3,5,7,9

### 10. None
Python: x = None //type(x) = NoneType
C++: nullptr



account_balance = '12'

isinstance(account_balance, int) # False
account_balance = 12
isinstance(account_balance, (int, float)) # True

## Function:
C++: void hello()
Python: def hello()