"""
Inheritence allows to define classes that inherit all the methods and properties from another class.

Parent class: also called the base class, from which Child or derived class inherits
Child class: also called derived class inherits from another class.

"""

class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def __str__(self):
        return f"First Name: {self.fname} \nLast Name: {self.lname}"

person = Person("Muhammad", "Fahad")
print(person)


class Student(Person):
    def __init__(self, fname, lname, session):
        super().__init__(fname,lname)
        self.session = session

    def __str__(self):
        return f"{super().__str__()} \nSession: {self.session} - {self.session + 4}"

student=Student("Muhammad", "Fahad", 2020)

print(student)
