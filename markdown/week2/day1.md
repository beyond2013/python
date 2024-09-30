# 1. Python Syntax: No Semicolons, Indentation, No Parentheses

**No Semicolons:**
- Unlike other programming languages such as C++ or Java, Python does not require a semicolon (`;`) to end statements.
- Statements are automatically ended by line breaks, which makes the syntax cleaner and easier to read.

```python
# Python statement without semicolon
print("Hello, Python")
```

**Practical Activity:**
- Write a simple program to print "Hello, World!" without using semicolons.

---

# Example of indentation in a function

```python
def greet():
    print("Hello!")
    print("Welcome to Python")

# Calling the function
greet()
```

**Practical Activity:**
- Write a Python function that prints a greeting message using proper indentation.

---

**No Parentheses in Control Structures:**
- Python does not require parentheses around conditions in `if`, `while`, and `for` loops (though they can be used optionally).
- Control structures rely on indentation rather than braces.

```python
# Example of an if statement without parentheses
x = 10
if x > 5:
    print("x is greater than 5")
```

**Practical Activity:**
- Write a simple `if-else` statement to check if a number is positive, negative, or zero without using parentheses.

---

### 2. PEP 8 Style Guide: Writing Readable Code

**What is PEP 8?**
- PEP 8 is Python’s official style guide that provides coding conventions for writing readable and maintainable code.
- Following PEP 8 ensures consistency in code formatting, making it easier to collaborate with other developers.

**Key PEP 8 Guidelines:**
- **Indentation:** Use 4 spaces per indentation level (never use tabs).
- **Line Length:** Limit lines to a maximum of 79 characters.
- **Blank Lines:** Use blank lines to separate functions and class definitions.
- **Comments:** Use comments to explain the purpose of complex code.
- **Variable Names:** Use lowercase letters, with words separated by underscores (`snake_case`).

```python
# Example of PEP 8 compliant code
def add_numbers(a, b):
    """
    Add two numbers and return the result.
    """
    return a + b

result = add_numbers(5, 10)
print(result)
```

**Practical Activity:**
- Rewrite a basic Python function following the PEP 8 style guide, ensuring proper use of indentation, line length, and comments.

---

### 3. Keywords in Python

**What are Keywords?**
- Keywords are reserved words in Python that have a special meaning and cannot be used as variable names or identifiers.
- Examples of keywords include `if`, `else`, `for`, `while`, `def`, and `class`.

**Listing All Keywords:**
- Python provides the `keyword` module to list all current keywords.

```python
# List all Python keywords
import keyword
print(keyword.kwlist)
```

**Practical Activity:**
- Run a Python program to list all the reserved keywords.

---

### 4. Variables and Literals

**Variables:**
- Variables in Python are used to store data values.
- Variable names must begin with a letter (a-z, A-Z) or an underscore, followed by letters, digits, or underscores.

```python
# Example of defining variables
x = 5
y = "Python"
```

**Practical Activity:**
- Define three variables: one to store a number, another to store a string, and a third to store a floating-point number.

---

**Literals:**
- Literals are constant values that are assigned to variables. They can be of different types:
  - **Numeric Literals:** Integers, floating-point numbers, or complex numbers.
  - **String Literals:** Sequence of characters enclosed in single or double quotes.
  - **Boolean Literals:** `True` or `False` values.
  - **None Literal:** Represents the absence of a value.

```python
# Example of different types of literals
x = 10  # Numeric literal
y = 3.14  # Floating-point literal
z = "Hello, World!"  # String literal
is_valid = True  # Boolean literal
no_value = None  # None literal
```

**Practical Activity:**
- Write a program that demonstrates the use of different types of literals by assigning them to variables and printing them.

---

This lecture covers the essential syntax and coding standards for Python, providing participants with a solid foundation to write clean and readable code.