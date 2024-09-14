# 1. Introduction to Python Standard Library

**What is the Python Standard Library?**

- A collection of modules and packages that come pre-installed with Python.
- Offers tools for a wide range of tasks, from file handling to mathematical calculations.

**Why Use the Standard Library?**

- Saves development time by providing built-in solutions.
- Reduces the need for external dependencies.

## Practical Activity:
1. **Explore the Python Standard Library Documentation:**
   - Visit the [Python Standard Library documentation](https://docs.python.org/3/library/).
   - Navigate through the documentation to see what modules are available and briefly explore the ones that interest you.

---

## 2. Exploring Commonly Used Modules in Python Standard Library

### A. **os Module (Operating System Interface)**

**Overview:**

- Provides functions for interacting with the operating system, such as navigating the file system and executing system commands.

**Key Functions:**

- `os.getcwd()`: Get the current working directory.
- `os.listdir()`: List the contents of a directory.
- `os.mkdir()`: Create a new directory.

**Practical Activity:**

- Print the current working directory.
- List the contents of the current directory.
- Create a new directory named `test_dir`.

```python
import os

# Print current working directory
print("Current Directory:", os.getcwd())

# List contents of the directory
print("Directory Contents:", os.listdir())

# Create a new directory
os.mkdir('test_dir')
print("New Directory Created: test_dir")
```

### B. **sys Module (System-Specific Parameters and Functions)**

**Overview:**
- Allows interaction with the Python interpreter and system environment.

**Key Functions:**
- `sys.argv`: Command-line arguments passed to the script.
- `sys.exit()`: Exit from Python.
- `sys.version`: Get the Python version.

**Practical Activity:**
- Print the Python version and simulate receiving command-line arguments.

```python
import sys

# Print the Python version
print("Python Version:", sys.version)

# Simulate command-line arguments
print("Command-line Arguments:", sys.argv)
```

### C. **math Module (Mathematical Functions)**

**Overview:**
- Provides access to mathematical functions like trigonometry, logarithms, and constants such as π.

**Key Functions:**
- `math.sqrt()`: Calculate the square root.
- `math.factorial()`: Compute the factorial of a number.
- `math.pi`: Access the value of π.

**Practical Activity:**
- Calculate the square root and factorial of a given number.

```python
import math

# Calculate square root
num = 16
print(f"Square root of {num}:", math.sqrt(num))

# Calculate factorial
n = 5
print(f"Factorial of {n}:", math.factorial(n))

# Print the value of pi
print("Value of Pi:", math.pi)
```

---

## 3. Basic Concepts: Exception Handling

**What is Exception Handling?**

- A mechanism to handle runtime errors gracefully without crashing the program.

**Try-Except Block:**

- Use `try` to run code that might cause an error.
- Use `except` to handle the error and provide feedback.

**Practical Activity:**

- Write a program that catches division by zero errors and provides a custom error message.

```python
try:
    # Attempt to divide by zero
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
else:
    print("Result:", result)
finally:
    print("This block runs no matter what.")
```

---

## 4. Basic Concepts: File Handling

**What is File Handling?**

- Working with files in Python to read, write, or modify them.

**Opening and Closing Files:**

- Use `open()` to open a file.
- Use `close()` to close the file after the operation is complete.

**Modes of Opening Files:**

- `r`: Read mode (default).
- `w`: Write mode (overwrites).
- `a`: Append mode (adds to the end of the file).

**Practical Activity 1:**

- Write a program that writes a simple message to a file.

```python
# Open the file in write mode
file = open("sample.txt", "w")

# Write to the file
file.write("Hello, Python file handling!")

# Close the file
file.close()
```

**Practical Activity 2:**

- Read the contents of the file that was just written.

```python
# Open the file in read mode
file = open("sample.txt", "r")

# Read the contents of the file
content = file.read()
print("File Contents:", content)

# Close the file
file.close()
```

