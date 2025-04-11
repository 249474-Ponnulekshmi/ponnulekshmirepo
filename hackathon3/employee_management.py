'''
Author :- Ponnulekshmi P 
UID :- 249474
Date :- 11/04/2025
Description:-   Python file for Employee Management System Operations.

'''

# Import the functions from employee.py

from employee import Employee

# Class creation for Employee management

class Employeemanagement(object):
    
    def __init__(self):
        self.employee_list = []
        
# Operation 1 :- Adding details of a new employee    
    def add_employee(self, name, department, designation, gross_salary, tax, bonus):
        emp = Employee(name, department, designation, gross_salary, tax, bonus)
        self.employee_list.append(emp)
        return emp
    
# Operation 2:- View all details of employees
    def view_details(self):
        return self.employee_list
    
# Operation 3:- Search an employee by ID
    def search_by_id(self, search_id):
        for emp in self.employee_list:
            if emp.emp_id == search_id:
                return emp
        return None
    
# Operation 4:- Delete an employee using Name
    def delete_by_name(self, name):
        for emp in self.employee_list:
            if emp.name == name:
                self.employee_list.remove(emp)
                return True
        return False


    def load_emp_details(self, new_dict):
        self.employee_list = [Employee.from_dict(val) for val in new_dict]

   
    def to_dict_list(self):
        return [employee.write_to_dict() for employee in self.employee_list]