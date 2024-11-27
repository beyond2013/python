# Day2: Starting Out with Expressions

**What is an Expression?**

- An expression in Python is a combination of values, variables, operators, and function calls that can be evaluated to produce a result.

**Example of Expressions:**

```python
# Simple mathematical expression
result = 5 + 3 * 2
print(result)  # Output: 11
```

- Expressions can include:

  - **Literals**: Constant values like `5`, `True`, or `"hello"`.
  - **Variables**: Named references that store data.
  - **Operators**: Symbols that perform operations like `+`, `-`, `*`, `/`.

**Practical Activity:**

- Write a Python program that performs the following expression: `10 + 5 * 3 - 2 / 4` and print the result.

---

## 2. Basic Types in Python

Python provides several built-in data types. These are the building blocks for working with data in a Python program.

### **a. Integer (int):**
- Used to represent whole numbers.

```python
x = 10
print(type(x))  # Output: <class 'int'>
```

### **b. Floating-Point Number (float):**
- Used to represent decimal or fractional numbers.

```python
y = 3.14
print(type(y))  # Output: <class 'float'>
```

### **c. String (str):**
- Represents a sequence of characters (text).

```python
name = "Python"
print(type(name))  # Output: <class 'str'>
```

### **d. Boolean (bool):**
- Represents a logical value: either `True` or `False`.

```python
is_valid = True
print(type(is_valid))  # Output: <class 'bool'>
```

**Practical Activity:**
- Write a Python program that defines variables of each type: integer, float, string, and boolean. Print the value and type of each variable.

---

## 3. Working with Variables

**What are Variables?**
- Variables are containers for storing data values. They are created the moment a value is assigned to them.
- Variables do not require explicit declaration, and their data type is inferred based on the assigned value.

```python
# Variable assignment
age = 25
greeting = "Hello, Python"
is_active = True
```

**Variable Naming Rules:**
- Must start with a letter (a-z, A-Z) or an underscore (_), followed by letters, numbers, or underscores.
- Variables are case-sensitive (e.g., `age` and `Age` are different variables).
  
**Example:**
```python
# Valid variable names
first_name = "John"
age_25 = 25

# Invalid variable names
2nd_name = "Error"  # Starts with a number
my-name = "Error"   # Hyphen is not allowed
```

### **Updating Variables:**
- You can update the value of a variable after it’s been created.

```python
x = 10
x = x + 5  # Now x equals 15
print(x)
```

### **Variable Reassignment and Dynamic Typing:**
- In Python, variables can change their data type during execution.

```python
x = 10  # x is an integer
x = "Now I'm a string!"  # x is now a string
print(x)
```

**Practical Activity:**
- Write a Python program that assigns a value to a variable, prints it, changes the value, and then prints the updated value.

---

### Recap of Concepts:
- **Expressions** involve values, variables, and operators.
- Python has basic data types like `int`, `float`, `str`, and `bool`.
- **Variables** store data and are dynamically typed, meaning they can hold different types of values over time.

By practicing these fundamental concepts, you’ll build a strong foundation for writing more complex Python programs in the coming sessions.