# Programming Fundamentals
# Lecture: Loops in Python

---

# Learning Outcomes

By the end of this lecture, students will be able to:

- Explain the need for loops in programming.
- Differentiate between `while` and `for` loops.
- Use loops to solve repetitive problems.
- Trace the execution of loop statements.
- Develop simple Python programs using loops and decision structures.

---

# 1. Introduction to Loops

A computer can perform repetitive tasks very efficiently. In programming, we often need to execute the same set of instructions multiple times.

Consider the following situation:

Suppose a teacher wants to print "Welcome to Programming Fundamentals" 10 times.

Without loops:

```python
print("Welcome to Programming Fundamentals")
print("Welcome to Programming Fundamentals")
print("Welcome to Programming Fundamentals")
print("Welcome to Programming Fundamentals")
print("Welcome to Programming Fundamentals")
print("Welcome to Programming Fundamentals")
print("Welcome to Programming Fundamentals")
print("Welcome to Programming Fundamentals")
print("Welcome to Programming Fundamentals")
print("Welcome to Programming Fundamentals")
```

This approach is inefficient.

Loops allow us to repeat instructions automatically.

---

# 2. What is a Loop?

A loop is a control structure that repeatedly executes a block of code until a specified condition is met.

General idea:

```
Start
   ↓
Check Condition
   ↓
True → Execute Statements
   ↓
Update Loop Variable
   ↓
Check Condition Again
   ↓
False → Exit Loop
```

---

# 3. Types of Loops in Python

Python provides two main looping structures:

1. `while` loop
2. `for` loop

---

# 4. The While Loop

A `while` loop continues executing as long as its condition remains true.

## Syntax

```python
while condition:
    statements
```

---

# Example 1: Print Numbers from 1 to 5

```python
count = 1

while count <= 5:
    print(count)
    count = count + 1
```

### Output

```
1
2
3
4
5
```

---

# Understanding the Execution

Initial value:

```
count = 1
```

Loop execution:

| Iteration | Condition | Output | New Value |
|------------|------------|---------|------------|
| 1 | 1 <= 5 | 1 | 2 |
| 2 | 2 <= 5 | 2 | 3 |
| 3 | 3 <= 5 | 3 | 4 |
| 4 | 4 <= 5 | 4 | 5 |
| 5 | 5 <= 5 | 5 | 6 |
| 6 | 6 <= 5 | False | Stop |

---

# 5. Importance of Updating the Loop Variable

Consider:

```python
count = 1

while count <= 5:
    print(count)
```

The value of `count` never changes.

Condition always remains true.

This creates an Infinite Loop.

---

# Infinite Loop

An infinite loop never terminates.

Example:

```python
while True:
    print("Hello")
```

Output:

```
Hello
Hello
Hello
Hello
...
```

The program continues forever unless manually stopped.

---

# Example 2: Print Even Numbers from 2 to 20

```python
num = 2

while num <= 20:
    print(num)
    num = num + 2
```

### Output

```
2
4
6
8
10
12
14
16
18
20
```

---

# Example 3: Countdown Timer

```python
count = 10

while count >= 1:
    print(count)
    count = count - 1

print("Blast Off!")
```

### Output

```
10
9
8
7
6
5
4
3
2
1
Blast Off!
```

---

# 6. Accumulator Pattern

Often we need to calculate totals.

An accumulator is a variable that stores a running total.

---

# Example 4: Sum of Numbers from 1 to 5

```python
count = 1
total = 0

while count <= 5:
    total = total + count
    count = count + 1

print("Sum =", total)
```

### Output

```
Sum = 15
```

---

# Real-World Example: Total Shopping Cost

```python
items = 1
total_cost = 0

while items <= 3:
    price = float(input("Enter item price: "))
    total_cost = total_cost + price
    items = items + 1

print("Total Cost =", total_cost)
```

---

# 7. The For Loop

A `for` loop is used when the number of repetitions is known.

Python commonly uses the `range()` function with `for` loops.

---

# Syntax

```python
for variable in range(...):
    statements
```

---

# Example 5: Print Numbers from 1 to 5

```python
for num in range(1, 6):
    print(num)
```

### Output

```
1
2
3
4
5
```

---

# Understanding range()

## Form 1

```python
range(stop)
```

Example:

```python
for i in range(5):
    print(i)
```

Output:

```
0
1
2
3
4
```

---

## Form 2

```python
range(start, stop)
```

Example:

```python
for i in range(1, 6):
    print(i)
```

Output:

```
1
2
3
4
5
```

---

## Form 3

```python
range(start, stop, step)
```

Example:

```python
for i in range(2, 21, 2):
    print(i)
```

Output:

```
2
4
6
8
10
12
14
16
18
20
```

---

# Example 6: Countdown

```python
for i in range(10, 0, -1):
    print(i)

print("Blast Off!")
```

### Output

```
10
9
8
7
6
5
4
3
2
1
Blast Off!
```

---

# 8. Comparing While and For Loops

## While Loop

Used when repetitions are not known beforehand.

Example:

```python
password = ""

while password != "python":
    password = input("Enter Password: ")
```

---

## For Loop

Used when repetitions are known.

Example:

```python
for i in range(10):
    print(i)
```

---

# 9. Using If Statements Inside Loops

Loops and branching are frequently used together.

---

# Example 7: Check Even or Odd Numbers

```python
for i in range(1, 11):

    if i % 2 == 0:
        print(i, "is Even")
    else:
        print(i, "is Odd")
```

### Output

```
1 is Odd
2 is Even
3 is Odd
...
10 is Even
```

---

# Example 8: Count Passing Students

```python
passes = 0

for i in range(1, 6):

    marks = int(input("Enter marks: "))

    if marks >= 50:
        passes = passes + 1

print("Number of Passes =", passes)
```

---

# Real-World Example: Plot Pricing

Suppose land costs Rs. 8,000 per square foot.

The user enters dimensions of multiple plots and the program calculates their values.

```python
price_per_sqft = 8000

for plot in range(1, 4):

    length = float(input("Enter length: "))
    width = float(input("Enter width: "))

    area = length * width
    value = area * price_per_sqft

    print("Plot Area =", area)
    print("Plot Value =", value)
```

---

# 10. Nested Loops (Introduction)

A loop inside another loop is called a nested loop.

Example:

```python
for row in range(3):

    for col in range(4):
        print("*", end=" ")

    print()
```

Output:

```
* * * *
* * * *
* * * *
```

---

# Common Mistakes

## Missing Colon

Incorrect:

```python
while count <= 5
```

Correct:

```python
while count <= 5:
```

---

## Forgetting Update Statement

Incorrect:

```python
count = 1

while count <= 5:
    print(count)
```

Leads to an infinite loop.

---

## Incorrect Indentation

Incorrect:

```python
for i in range(5):
print(i)
```

Correct:

```python
for i in range(5):
    print(i)
```

---

# Summary

- Loops are used to repeat statements.
- Python provides `while` and `for` loops.
- `while` loops are condition-controlled.
- `for` loops are count-controlled.
- `range()` is commonly used with `for` loops.
- Loops can be combined with `if` statements.
- Accumulators help calculate totals.
- Incorrect updates may create infinite loops.

---

# Practice Exercises

### Exercise 1

Print numbers from 1 to 20 using a `while` loop.

---

### Exercise 2

Print all odd numbers from 1 to 25 using a `for` loop.

---

### Exercise 3

Calculate the sum of numbers from 1 to 100.

---

### Exercise 4

Input marks of 5 students and count how many students passed.

---

### Exercise 5

Print the multiplication table of a number entered by the user.

Example:

```
Enter Number: 7

7 × 1 = 7
7 × 2 = 14
...
7 × 10 = 70
```

---

# Lab Activity

Write a Python program that:

1. Inputs marks of 10 students.
2. Counts the number of passed students (marks ≥ 50).
3. Counts the number of failed students.
4. Calculates the average marks.
5. Displays all results at the end.

Expected Concepts:

- Loop
- Variables
- Accumulator
- Counter
- If-Else
- Input/Output
