# Author: Stephen Neville adapted from playing with code examples from stackoverflow
from datetime import date

class Employee:
    """
    A class for Employee is created
    """
    def __init__(self, first, last, yearborn, monthborn, dayborn, pay):
        """
        A constructor to instantiate each employee object

        """
        self.first = first
        self.last = last                                    
        self.born = date(yearborn, monthborn,dayborn)
        self.pay = pay
        self.email = first + "." + last + "@somebusiness.com"
                                     
    def fullname(self):
        """
        This is a method to create a fullname. Just like a function.
        """
        return "{} {}".format(self.first, self.last)
                                     
    def calculate_age(self):
        """
        This is a method to calculate the age from the date of birth of employee
        """
        today = date.today()
        return today.year - self.born.year - ((today.month, today.day) < (self.born.month, self.born.day))

# Creates the object emp_1
emp_1 = Employee("Tom","Jones",1945,3,28, 10000)

print(emp_1.fullname())

print(emp_1.email)

print(emp_1.calculate_age())

