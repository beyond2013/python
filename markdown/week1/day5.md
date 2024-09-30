# 1. Introduction to Object-Oriented Programming (OOP)

**What is Object-Oriented Programming?**

- OOP is a programming paradigm based on the concept of "objects," which can contain data (attributes) and code (methods) to manipulate that data.

**Key Concepts of OOP:**

- **Class:** A blueprint for creating objects (a specific data structure).
- **Object:** An instance of a class.
- **Inheritance:** The ability to create a new class that inherits the attributes and methods from another class.


## 2. Classes and Objects in Python

**Defining a Class:**

- A class is defined using the `class` keyword, followed by the class name. Classes can contain attributes (variables) and methods (functions).

```python
class Car:
    def __init__(self, make, model, year):
        # Constructor to initialize the attributes
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        # Method to display car information
        print(f"Car: {self.year} {self.make} {self.model}")
```

**Creating an Object:**

- An object is created by calling the class and passing arguments to its constructor.

```python
# Creating an object of the Car class
my_car = Car("Toyota", "Corolla", 2022)

# Accessing the object's method
my_car.display_info()
```


## 3. Inheritance in Python

**What is Inheritance?**
- Inheritance allows one class (the child or subclass) to inherit the attributes and methods of another class (the parent or superclass).

**Single Inheritance Example:**
- The child class can add or override methods and attributes of the parent class.

```python
# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

# Child class inheriting from Animal
class Dog(Animal):
    def speak(self):
        # Overriding the speak method
        print(f"{self.name} barks.")

# Creating an object of the Dog class
dog = Dog("Buddy")
dog.speak()
```

**Why Use Inheritance?**
- Inheritance promotes code reuse by allowing new classes to adopt the behavior of existing ones without rewriting code.


# 4. Command-Line Project: A Student Management System

This simple project will combine the concepts of:
- Setting up Python environments (Day 2)
- Functions, modules, and libraries (Day 3)
- File handling, exception handling (Day 4)
- Object-oriented programming (Day 5)

**Project Overview:**
Create a command-line Student Management System that allows users to:
- Add new students.
- View student details.
- Save and retrieve student data from a file.
- Handle exceptions when reading or writing files.

**Step-by-Step Breakdown:**

1. **Set Up Virtual Environment:**
   - Create a virtual environment and activate it.

2. **Define the Student Class:**
   - Define a class `Student` with attributes like `name`, `roll_no`, and `grade`.

3. **Write Methods for Student Class:**
   - Implement methods for displaying student information and saving student data to a file.

4. **Add Exception Handling:**
   - Add exception handling for cases where file operations may fail.

5. **File Handling:**
   - Store student information in a text file using file handling.

6. **Modules and Libraries:**
   - Organize the code into functions and modules for better readability.

**Project Code Example:**

```python
import os

class Student:
    def __init__(self, name, roll_no, grade):
        self.name = name
        self.roll_no = roll_no
        self.grade = grade

    def display_info(self):
        print(f"Student Name: {self.name}, Roll No: {self.roll_no}, Grade: {self.grade}")

    def save_to_file(self, file_name):
        try:
            with open(file_name, "a") as file:
                file.write(f"{self.name}, {self.roll_no}, {self.grade}\n")
        except IOError:
            print("Error: Could not write to file.")

def load_students(file_name):
    try:
        with open(file_name, "r") as file:
            students = file.readlines()
            for student in students:
                print(student.strip())
    except FileNotFoundError:
        print(f"No records found in {file_name}.")
    except IOError:
        print("Error: Could not read file.")

# Main Program
def main():
    file_name = "students.txt"
    
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            name = input("Enter student name: ")
            roll_no = input("Enter student roll number: ")
            grade = input("Enter student grade: ")
            
            student = Student(name, roll_no, grade)
            student.save_to_file(file_name)
        
        elif choice == "2":
            load_students(file_name)
        
        elif choice == "3":
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```

This project reinforces the topics covered throughout the week, including:
- Setting up the development environment.
- Using functions and modules.
- Exception and file handling.
- Implementing object-oriented programming concepts like classes, objects, and inheritance.