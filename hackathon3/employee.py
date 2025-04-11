'''
Author :- Ponnulekshmi P 
UID :- 249474
Date :- 11/04/2025
Description:-   Creating an Employee Management System using OOPs Concepts.
                Consists of Class creation for employee including required arguments.
'''

import uuid     # For generating uuid

# Class creation for Employee with arguments name, department, designation, gross_salary, tax, bonus, emp_id

class Employee(object):
    
    def __init__(self, name, department, designation, gross_salary, tax, bonus, emp_id = None):
        
        self.name = name
        self.department = department
        self.designation = designation
        self.gross_salary = gross_salary
        self.tax = tax
        self.bonus = bonus
        self.emp_id = emp_id if emp_id else str(uuid.uuid4())
        self.net_salary = self.calculate_net_salary()
        
# Function defiinition to represent the output as string

    def __str__(self):
        return(f"Employee ID : {self.emp_id}, Name : {self.name}, Department : {self.department}, Designation : {self.designation}, Gross Salary : {self.gross_salary}, Tax : {self.tax}, Bonus : {self.bonus}, Net Salary : {self.net_salary}")

# Function to calculate net salary

    def calculate_net_salary(self):
        amount = self.gross_salary * (self.tax / 100)
        return self.gross_salary - amount + self.bonus

# Function to write the employee data to dictionary

    def write_to_dict(self):
        return {
            "Employee ID" : self.emp_id, 
            "Name" : self.name, 
            "Department" : self.department, 
            "Designation" : self.designation,
            "Gross_Salary" : self.gross_salary,
            "Tax" : self.tax, 
            "Bonus"  : self.bonus, 
            "Net_Salary" : self.net_salary       
        }
    
# Static Method 
    @staticmethod
    def from_dict(emp_data):
        return Employee(
            name = emp_data["Name"],
            department = emp_data["Department"],
            designation = emp_data["Designation"],
            gross_salary = emp_data["Gross_Salary"],
            tax = emp_data["Tax"],
            bonus = emp_data["Bonus"],
            emp_id = emp_data["Employee ID"]
        )

    