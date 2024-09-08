# Day 2: Python Vocational Training Program

## 1. Installing the Latest Stable Release of Python

**Step-by-Step Guide:**

1. **Determine Your Windows Architecture:**

   - **Open the Start Menu:**
     - Click on the **Start** button (Windows icon) in the bottom-left corner of your screen.
   - **Go to Settings:**
     - Click on the **Settings** gear icon.
   - **Access System Information:**
     - Navigate to **System > About**.
   - **Check System Type:**
     - Look for "System type" under "Device specifications."  
     - It will show either "64-bit operating system" or "32-bit operating system."

2. **Download the Latest Python Installer:**

   - If you have a **64-bit operating system**, [download Python 3.12.0 (64-bit)](https://www.python.org/ftp/python/3.12.0/python-3.12.0-amd64.exe).
   - If you have a **32-bit operating system**, [download Python 3.12.0 (32-bit)](https://www.python.org/ftp/python/3.12.0/python-3.12.0.exe).

3. **Run the Installer:**

   - Double-click the downloaded file.
   - Check the box for “Add Python to PATH.”
   - Click on "Install Now" and follow the on-screen instructions.

4. **Verify Installation:**

   - Open the Start Menu, search for "Python," and run the Python app.
   - A Python shell window should open, indicating that Python is installed correctly.


## 2. Setting Up Anaconda Distribution for Python

**Overview:**
Anaconda is a popular distribution that simplifies package management and deployment.

**Step-by-Step Guide:**

1. **Determine Your Windows Architecture:**

   - Follow the steps in the previous section to check your system type (32-bit or 64-bit).

2. **Download the Latest Anaconda Installer:**

   - If you have a **64-bit operating system**, [download Anaconda (64-bit)](https://repo.anaconda.com/archive/Anaconda3-2023.07-Windows-x86_64.exe).
   - If you have a **32-bit operating system**, [download Anaconda (32-bit)](https://repo.anaconda.com/archive/Anaconda3-2023.07-Windows-x86.exe).

3. **Run the Installer:**

   - Double-click the downloaded file.
   - Follow the installation instructions, choosing the default options.
   - Check the box to “Add Anaconda to my PATH environment variable.”

4. **Verify Installation:**

   - Open the Anaconda Navigator from the Start Menu to ensure it is installed correctly.


## 3. Installing Packages Using PIP

**What is PIP?**

- PIP is the package installer for Python.
- It allows you to install and manage additional packages that are not included in the Python standard library.

**Step-by-Step Guide:**

1. **Open the Python Shell:**  Search for "Python" in the Start Menu and open the Python app.
2. **Install a Package:** In the Python shell, type the command `!pip install package_name` (e.g., `!pip install numpy`) and press Enter.
3. **Verify Installation:** Type `!pip show package_name` (e.g., `!pip show numpy`) to confirm that the package is installed.

## **Activity: Your turn to use PIP**
- install popular packages like `numpy` and `pandas` using PIP.

## **4. Basic Concepts: Control Structures and Loops**

### **Introduction to Control Structures:**

- **If, Else, Elif Statements:**
  - Syntax:

    ```python
    if condition:
        # code to execute if condition is true
    elif another_condition:
        # code to execute if the above condition is false and this one is true
    else:
        # code to execute if all conditions are false
    ```
  - **Example:**

    ```python
    temperature = 12
    if temperature < 0:
        print("Cold")
    elif age > 32 :
        print("Hot")
    else:
        print("Pleasant")
    ```

### **Introduction to Loops:**

- **For Loop:**

  - Used to iterate over a sequence (like a list, tuple, dictionary, set, or string).
  - **Syntax:**

    ```python
    for variable in sequence:
        # code to execute repeatedly
    ```
  - **Example:**

    ```python
    for i in range(5):
        print(i)
    ```
- **While Loop:**
  - Repeats a block of code as long as a condition is true.
  - **Syntax:**

    ```python
    while condition:
        # code to execute repeatedly
    ```
  - **Example:**

    ```python
    count = 0
    while count < 5:
        print(count)
        count += 1
    ```

### **Activity:**

  - Write a Python program that prints:
  1. all even numbers form 1 to 20.
  2. all odd numbers from 1 to 20.
  3. all prime numbers between 2 and 100.


## **Q&A Session:**

-  Please ask any question to clarify any doubts about today's topics.

