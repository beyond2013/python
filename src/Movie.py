"""
   Almost anything in python is an object, with its properties and methods.
   Class: is like a blueprint for creating Objects

"""


class Movie:
    """
     1. __init__ is a special function which is automatically called 
        every time the class is being used to create a new object

    2. the self parameter is a reference to the current instance of 
       the class
       naming it self is not mandatory, but it has to be the first parameter
    """
    def __init__(self, name, released):
        self.name = name
        self.released = released
    """
    the __str__() function controls what should be returned when 
    the class object is represented as a string
    """

    def __str__(self):
        return f"{self.name}({self.released})"

movie1=Movie("The good, the bad and the ugly",1966)

print(movie1)
