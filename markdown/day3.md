# Day 3: Setting Up Virtual Environments for Python Projects

## Objective:
By the end of this session, participants will:
- Set up virtual environments for Python projects.
- Gain an overview of popular Python IDEs and text editors.
- Understand basic Python programming concepts, including functions, modules, and libraries.

## 1. Setting Up Virtual Environments for Python Projects

**What is a Virtual Environment?**

- A virtual environment is a self-contained directory that contains a specific Python installation and any packages required for a particular project.
- It prevents conflicts between dependencies in different projects.

**Step-by-Step Guide:**

1. **Install `virtualenv` (if not already installed):**

   - Open the Command Prompt or Anaconda Prompt and type:
     ```cmd
     pip install virtualenv
     ```

2. **Create a Virtual Environment:**

   - Navigate to your project folder or create a new one.
   - Type:
     ```cmd
     python -m venv env_name
     ```

3. **Activate the Virtual Environment:**

   - For Windows:
     ```cmd
     env_name\Scripts\activate
     ```

4. **Deactivate the Virtual Environment:**

   - When you’re done working in the environment, type:
     ```cmd
     deactivate
     ```

5. **Installing Packages in the Virtual Environment:**

   - While the environment is active, you can install packages using PIP:
     ```cmd
     pip install package_name
     ```

## Activity:

- Create a virtual environment, activate it, install a package, and then deactivate the environment.


## 2. Overview of Python IDEs and Text Editors

**Why Use an IDE or Text Editor?**
Integrated Development Environments (IDEs) and text editors help developers write and manage their code more efficiently by providing features such as syntax highlighting, debugging, and project management.

**Popular Python IDEs and Text Editors:**

1. **Jupyter Notebooks:**

   - **Best for:** Data science, education, interactive programming.
   - **Features:** Interactive coding with Markdown support and inline data visualization.
   - **How to Access:**
     - Installed with Anaconda or via PIP: `pip install jupyterlab`.
     - Run from Anaconda Navigator or via command line: `jupyter notebook`.

2. **PyCharm (Community Edition):**

   - **Best for:** Full-featured Python development.
   - **Features:** Auto-completion, debugging, project navigation, version control.
   - **Installation:**
     - Download and install from [PyCharm Community Edition](https://www.jetbrains.com/pycharm/download/).
   
3. **Spider (Scientific Python Development Environment):**

   - **Best for:** Scientific programming and data analysis.
   - **Features:** MATLAB-like interface, with variable explorer, IPython console, and code editor.
   - **Installation:**
     - Available with Anaconda or install via PIP: `pip install spyder`.

## Activity:
- Explore one of these tools, depending on your interests and project needs.

---

## 3. Basic Concepts: Functions, Modules, and Libraries

## Functions:

Functions allow you to encapsulate reusable blocks of code. They make the program modular, reducing redundancy.

- **Defining a Function:**

  ```python
  def function_name(parameters):
      # block of code
      return value
  ```

- **Example:**

  ```python
  def greet(name):
      return f"Hello, {name}!"
  
  print(greet("Alice"))  # Output: Hello, Alice!
  ```

## Modules:

- Modules are Python files that contain definitions and statements.
- They allow you to logically organize your code.

- **Creating a Module:**

  - Simply save your Python file with a `.py` extension. For example, `mymodule.py` can be used as:
    ```python
    import mymodule
    ```

- **Example:**
  ```python
  # mymodule.py
  def square(num):
      return num * num
  ```

  ```python
  # main.py
  import mymodule
  print(mymodule.square(5))  # Output: 25
  ```

## Libraries:
Libraries are collections of modules that offer a wide range of functionality, from handling files to performing complex computations.

- **Common Libraries:**
  - **NumPy:** For numerical operations.
  - **Pandas:** For data analysis.
  - **Matplotlib:** For plotting.
  
  **Installing Libraries:**
  ```bash
  pip install numpy pandas matplotlib
  ```

## **Activity:**
- Define a function, create a module, and use an external library like `numpy` to perform a small calculation.

---

## **Q&A and Discussion:**
-  Please ask any question to clarify any doubts about today's topics.

## Practice 
- Create a simple Python project that includes:
  - A virtual environment.
  - A function inside a module.
  - Use of at least one external library (e.g., `numpy` or `pandas`).

