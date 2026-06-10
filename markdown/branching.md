# Programming Fundamentals
# Lecture: Branching and Decision Making in Python

---

# Learning Outcomes

By the end of this lecture, students will be able to:

- Understand the need for decision making in programs
- Explain the concept of branching
- Use the `if` statement in Python
- Use the `if-else` statement in Python
- Use the `if-elif-else` ladder in Python
- Understand the equivalent of a switch/case statement in Python
- Trace program execution through different branches
- Develop simple decision-making programs

---

# 1. Introduction: Why Do We Need Branching?

So far, our programs have executed statements sequentially.

Example:

```python
print("Step 1")
print("Step 2")
print("Step 3")
```

Output:

```text
Step 1
Step 2
Step 3
```

The statements always execute in the same order.

This type of execution is called **sequential execution**.

However, many real-world situations require decisions.

Examples:

- If a student scores above 50, declare "Pass".
- If a user enters the correct password, allow login.
- If temperature is high, turn on the fan.
- If balance is insufficient, reject withdrawal.

Programs must therefore be able to choose between alternative actions.

This leads us to **branching**.

---

# 2. What is Branching?

Branching is the process of selecting one path from multiple possible paths based on a condition.

Consider the following situation:

```text
                Is it raining?
                      |
            -------------------
            |                 |
          Yes               No
            |                 |
      Take Umbrella      Do not take Umbrella
```

The program evaluates a condition and follows the appropriate path.

---

# 3. Conditions and Boolean Expressions

A condition is an expression that evaluates to either:

```python
True
```

or

```python
False
```

Examples:

```python
5 > 3
```

Result:

```python
True
```

---

```python
10 < 4
```

Result:

```python
False
```

---

## Relational Operators

| Operator | Meaning |
|-----------|----------|
| > | Greater than |
| < | Less than |
| >= | Greater than or equal to |
| <= | Less than or equal to |
| == | Equal to |
| != | Not equal to |

Examples:

```python
10 > 5
```

```python
20 == 20
```

```python
7 != 9
```

---

# 4. The if Statement

The simplest form of branching is the `if` statement.

## Syntax

```python
if condition:
    statement(s)
```

If the condition is True, the statements execute.

If the condition is False, they are skipped.

---

## Control Flow

```text
            Condition
                |
          True / \ False
              /   \
             /     \
      Execute     Skip
      Statements
```

---

## Example 1

```python
age = 20

if age >= 18:
    print("You can vote")
```

Output:

```text
You can vote
```

---

## Example 2

```python
age = 15

if age >= 18:
    print("You can vote")
```

Output:

```text
(No output)
```

The condition is False, so the statement is skipped.

---

## Example 3

```python
number = int(input("Enter a number: "))

if number > 0:
    print("Positive Number")
```

---

# 5. Importance of Indentation

Python uses indentation instead of braces `{}`.

Correct:

```python
if x > 0:
    print("Positive")
```

Incorrect:

```python
if x > 0:
print("Positive")
```

This causes an error.

---

# Limitation of if Statement

Suppose we want to display:

- "Pass" if marks ≥ 50
- "Fail" otherwise

Using only `if` is not sufficient because we need two alternative actions.

This leads us to the `if-else` statement.

---

# 6. The if-else Statement

The `if-else` statement provides two possible paths.

## Syntax

```python
if condition:
    statements_if_true
else:
    statements_if_false
```

---

## Control Flow

```text
                 Condition
                     |
              ----------------
              |              |
            True          False
              |              |
      Execute IF      Execute ELSE
```

---

## Example 1

```python
marks = 70

if marks >= 50:
    print("Pass")
else:
    print("Fail")
```

Output:

```text
Pass
```

---

## Example 2

```python
marks = 35

if marks >= 50:
    print("Pass")
else:
    print("Fail")
```

Output:

```text
Fail
```

---

## Example 3: Even or Odd

```python
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

---

## Example 4: Voting Eligibility

```python
age = int(input("Enter age: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")
```

---

# Limitation of if-else

Suppose we want to classify marks as:

- A Grade
- B Grade
- C Grade
- Fail

Two branches are not enough.

We need multiple conditions.

This leads us to the `if-elif-else` ladder.

---

# 7. The if-elif-else Ladder

Python uses `elif` (else if) to test multiple conditions.

## Syntax

```python
if condition1:
    statements1

elif condition2:
    statements2

elif condition3:
    statements3

else:
    statements4
```

---

## Control Flow

```text
          Condition 1
             |
      True ----- False
       |           |
 Action 1    Condition 2
                  |
           True ----- False
             |          |
        Action 2   Condition 3
                        |
                 True ----- False
                   |          |
              Action 3    Else
```

---

## Example 1: Grade Calculation

```python
marks = int(input("Enter marks: "))

if marks >= 80:
    print("Grade A")

elif marks >= 70:
    print("Grade B")

elif marks >= 50:
    print("Grade C")

else:
    print("Fail")
```

---

## Example Runs

Input:

```text
85
```

Output:

```text
Grade A
```

---

Input:

```text
72
```

Output:

```text
Grade B
```

---

Input:

```text
55
```

Output:

```text
Grade C
```

---

Input:

```text
30
```

Output:

```text
Fail
```

---

# Important Observation

Only one branch executes.

Consider:

```python
marks = 90

if marks >= 80:
    print("A")

elif marks >= 70:
    print("B")
```

Even though 90 is greater than both 80 and 70, only:

```text
A
```

is printed.

After finding a True condition, Python exits the ladder.

---

# 8. Nested if Statements

An `if` statement can contain another `if`.

## Example

```python
age = 25
citizen = True

if age >= 18:

    if citizen:
        print("Eligible to vote")
```

Output:

```text
Eligible to vote
```

---

# 9. Case Selection (Switch/Case Concept)

Many programming languages provide:

```text
switch-case
```

or

```text
case
```

statements.

Example in C/C++:

```cpp
switch(day)
{
    case 1:
        cout<<"Monday";
        break;

    case 2:
        cout<<"Tuesday";
        break;
}
```

Historically, Python did not have a switch statement.

Programmers used `if-elif-else` instead.

---

# 10. Python Match-Case Statement

Python 3.10 introduced:

```python
match-case
```

which serves a similar purpose to switch-case.

---

## Syntax

```python
match variable:

    case value1:
        statements

    case value2:
        statements

    case _:
        default_statements
```

The underscore `_` acts as the default case.

---

## Example: Day of Week

```python
day = int(input("Enter day number: "))

match day:

    case 1:
        print("Monday")

    case 2:
        print("Tuesday")

    case 3:
        print("Wednesday")

    case _:
        print("Invalid Day")
```

---

## Example Runs

Input:

```text
2
```

Output:

```text
Tuesday
```

---

Input:

```text
7
```

Output:

```text
Invalid Day
```

---

# When Should We Use Match-Case?

Use `match-case` when:

- Comparing a variable against many fixed values
- Building menus
- Handling user choices

Example:

```python
choice = int(input("Enter choice: "))

match choice:

    case 1:
        print("Add")

    case 2:
        print("Delete")

    case 3:
        print("Update")

    case _:
        print("Invalid Choice")
```

---

# Comparison of Branching Structures

| Structure | Purpose |
|------------|----------|
| if | One-way decision |
| if-else | Two-way decision |
| if-elif-else | Multiple decisions |
| match-case | Selection from fixed values |

---

# Real-Life Example

ATM Withdrawal:

```text
                Balance >= Amount?
                      |
               -------------------
               |                 |
             Yes                No
               |                 |
       Dispense Cash      Insufficient Funds
```

This can be implemented using:

```python
if balance >= amount:
    print("Cash Dispensed")
else:
    print("Insufficient Funds")
```

---

# Common Mistakes

## Mistake 1

Using = instead of ==

Wrong:

```python
if marks = 50:
```

Correct:

```python
if marks == 50:
```

---

## Mistake 2

Incorrect indentation

Wrong:

```python
if x > 0:
print("Positive")
```

Correct:

```python
if x > 0:
    print("Positive")
```

---

## Mistake 3

Incorrect order of conditions

Wrong:

```python
if marks >= 50:
    print("Pass")

elif marks >= 80:
    print("Grade A")
```

The second condition will never execute.

Correct:

```python
if marks >= 80:
    print("Grade A")

elif marks >= 50:
    print("Pass")
```

---

# Summary

In this lecture, we learned:

1. Programs normally execute sequentially.
2. Branching allows programs to make decisions.
3. Conditions evaluate to True or False.
4. `if` is used for one-way decisions.
5. `if-else` is used for two-way decisions.
6. `if-elif-else` is used for multiple alternatives.
7. Nested `if` statements allow decisions within decisions.
8. Python's `match-case` provides switch/case functionality.
9. Proper indentation is essential in Python.

Branching is one of the most important programming concepts because it allows programs to behave differently under different conditions and forms the basis of intelligent decision-making in software.