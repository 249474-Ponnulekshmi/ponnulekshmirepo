'''
HACKATHON - 02
Author :-  Ponnulekshmi P - 249474
Module preperation for Employee Management System

'''

import json

# Class creation for Person with attributes name, age and gender
class Person(object):
    
    # Constructor
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    # Methods
    def get_details(self):
        return ','.join([str(self.name), str(self.age), str(self.gender)])
    
# Class inherited from Person - named as Employee with attributes employee id, department, salary
class Employee(Person):
    
    # Constructor
    def __init__(self, name, age, gender, emp_id, department, salary):
        super().__init__(name, age, gender)
        self.emp_id = emp_id
        self.department = department
        self.salary = salary
        
    # Methods
    def get_details(self):
        parent_details = super().get_details()
        return ','.join([parent_details, str(self.emp_id), str(self.department), str(self.salary)])
    
    def is_eligible_for_bonus(self):
        if(self.salary < 50000):
            print("True")
            return True
        else:
            print("False")
            return False
        
    def to_dict(self):  
        return {
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "emp_id": self.emp_id,
            "department": self.department,
            "salary": self.salary
        }
    
    # Class Method
    def from_string(cls, data_string):
        name, age, gender, emp_id, department, salary = data_string.split(",")
        return cls(name, int(age), gender, emp_id, department, float(salary))
    
    from_string = classmethod(from_string)
    
    # Static Method
    def bonus_policy():
        print("____Company Bonus Policy____")
        print("-> Employees with salary less than INR 50000 is eligible for BONUSES")
        
    bonus_policy = staticmethod(bonus_policy)
    
'''

New Class - DEPARTMENT with attributes name and list of employees

'''
    
# Class creation for Department

class Department(object):
    
    # Constructor 
    def __init__(self, name, employees = None):
        self.name = name
        self.employees = employees if employees is not None else []
        
    # Methods
    def add_employee(self, emp):
        if isinstance(emp, Employee): 
            self.employees.append(emp)
        else:
            raise TypeError("Invalid Type.")
        
    def get_average_salary(self):
        if not self.employees:
            return 0
        total_salary = sum(emp.salary for emp in self.employees)
        self.avg_salary = total_salary/len(self.employees)
        return self.avg_salary
    
    def get_all_employees(self):
        return [emp.get_details() for emp in self.employees]
    


### Save all employee data to json file
def save_to_json(employees):    
    employees_dict_list = [employee.to_dict() for employee in employees]
    write_to_json = json.dumps(employees_dict_list, indent=4)
    with open("employee.json", "w") as f:
        f.write(write_to_json)
        
### Load from json file
def load_from_json():
    employees_list = []
    with open('employee.json', 'r') as file:
        employees_dict_list = json.load(file)
        
    for data in employees_dict_list:
        emp = Employee(
            name=data['name'],
            age=data['age'],
            gender=data['gender'],
            emp_id=data['emp_id'],
            department=data['department'],
            salary=data['salary']
        )
        employees_list.append(emp)
        
    return employees_list

            
            
        