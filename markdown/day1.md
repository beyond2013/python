# Day 1 Lecture: Introduction to Python

## I. Introduction to Python

**1. History of Python:**
  <img src="../fig/GuidoVanRossum.jpeg" align="right" height="250" width="250">
   - **Created By**: Python was created by [Guido van Rossum](https://www.youtube.com/watch?v=J0Aq44Pze-w) in the late 1980s, with its first release in 1991.
   - **Origin**: Named after the British comedy group "Monty Python." Guido van Rossum wanted a name that was unique, short, and slightly mysterious.
   - **Purpose**: Designed to be simple and easy to read, Python was intended to improve productivity and readability for software development.

**2. Significance of Python:**

   - **Ease of Learning**: Python’s syntax is clear and readable, making it an excellent choice for beginners.
   - **Versatility**: Python is a general-purpose language, suitable for web development, data analysis, automation, artificial intelligence, and more.
   - **Extensive Libraries and Frameworks**: Python offers a vast ecosystem of libraries and frameworks (like Django, Flask, NumPy, and Pandas) that accelerate development in various domains.

## II. Exploring Python's Popularity and Applications in Web Development

**1. Popularity of Python:**

   - **Most Loved Language**: According to various developer surveys (such as the Stack Overflow Developer Survey), Python consistently ranks as one of the most loved and widely used programming languages.
   - **Used by Top Companies**: Companies like Google, Netflix, Instagram, Dropbox, and Spotify use Python extensively in their technology stacks.

**2. Applications in Web Development:**

   - **Back-End Development**: Python is used to build server-side logic, APIs, and manage databases. Popular frameworks like **Django** and **Flask** make developing robust web applications efficient and scalable.
   - **Full-Stack Development**: Python can be part of a full-stack development setup when combined with front-end technologies.
   - **Automation and Scripting**: Python is ideal for writing scripts to automate repetitive tasks in web development, such as data scraping, testing, and deployment.

## III. Understanding Different Versions of Python

**1. Major Versions of Python:**

   - **Python 2.x**:
     - Released in 2000, Python 2.x was a significant upgrade that introduced many new features.
     - It is now considered legacy, with its final release (2.7) being in 2010 and official support ending in 2020.
   - **Python 3.x**:
     - Released in 2008, Python 3.x was not backward compatible with Python 2.x.
     - Major improvements include better support for Unicode, improved syntax, and new libraries. Python 3 is the recommended version for all new development.

**2. Minor Differences Between Python 2 and Python 3:**

   - **Print Statement**: In Python 2, `print` is a statement (`print "Hello"`). In Python 3, `print` is a function (`print("Hello")`).
   - **Integer Division**: In Python 2, dividing two integers performs floor division (`5 / 2` results in `2`). In Python 3, it results in a float (`5 / 2` results in `2.5`).
   - **Unicode Strings**: Python 3 treats all strings as Unicode by default, making it better suited for internationalization.

## IV. Basic Concepts of Python

**1. Variables in Python:**

   - **Definition**: A variable is a name that refers to a value stored in memory. It is used to store data that can be used and manipulated in a program.
   - **Declaration and Initialization**: Python does not require explicit declaration of variables; a variable is created the moment a value is assigned.
   - **Example**:
   ```python
   name = "John Doe"  # A string variable
   age = 30  # An integer variable
   height = 5.9  # A floating-point variable
   ```

**2. Data Types in Python:**

   - **Basic Data Types**:
     - **Integer (`int`)**: Represents whole numbers, e.g., `10`.
     - **Floating Point (`float`)**: Represents decimal numbers, e.g., `3.14`.
     - **String (`str`)**: Represents text, e.g., `"Hello, World!"`.
     - **Boolean (`bool`)**: Represents truth values, either `True` or `False`.
   - **Example**:
   ```python
   score = 85         # Integer
   average = 76.5     # Float
   message = "Python is fun!"  # String
   is_valid = True    # Boolean
   ```

**3. Basic Operations in Python:**

   - **Arithmetic Operations**:
     - Addition (`+`): Adds two numbers, e.g., `5 + 3` results in `8`.
     - Subtraction (`-`): Subtracts one number from another, e.g., `5 - 3` results in `2`.
     - Multiplication (`*`): Multiplies two numbers, e.g., `5 * 3` results in `15`.
     - Division (`/`): Divides one number by another, returning a float, e.g., `5 / 2` results in `2.5`.
     - Floor Division (`//`): Divides one number by another, discarding the remainder, e.g., `5 // 2` results in `2`.
     - Modulus (`%`): Returns the remainder of division, e.g., `5 % 2` results in `1`.
     - Exponentiation (`**`): Raises a number to the power of another, e.g., `5 ** 2` results in `25`.
   - **Example**:
   ```python
   a = 10
   b = 3
   sum = a + b          # 13
   difference = a - b   # 7
   product = a * b      # 30
   quotient = a / b     # 3.3333...
   floor_div = a // b   # 3
   remainder = a % b    # 1
   power = a ** b       # 1000
   ```

## Recap of Day 1 Topics:

   - Learned about Python's history, creators, and significance.
   - Explored Python's popularity and its applications in web development.
   - Understood different versions of Python and their minor differences.
   - Covered the basic concepts of Python, including variables, data types, and basic operations.

## Practical

- Write a Python script that converts a given length from feet to inches and inches to feet. Hint 1 foot = 12 inches
- Write a Python script that converts a temperature from Celsius to Fahrenheit and vice versa.
Hint: 
- To convert Celsius to Fahrenheit: $F=9/5×C+32$  
- To convert Fahrenheit to Celsius: $C=5/9×(F−32)$  

## **Q&A Session:**

-  Please ask any question to clarify any doubts about today's topics.