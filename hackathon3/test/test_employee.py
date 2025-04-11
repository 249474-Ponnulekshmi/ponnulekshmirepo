'''
Author :- Ponnulekshmi P 
UID :- 249474
Date :- 11/04/2025
Description:-   TEST CASES for Employee class
'''


import unittest
import uuid
from employee import Employee  

class TestEmployee(unittest.TestCase):

    def test_employee_creation_with_id(self):
        employee_id = str(uuid.uuid4())
        emp = Employee("Adithi", "IT", "Developer", 3600000, 5, 10000, emp_id=employee_id)
        
        self.assertEqual(emp.name, "Adithi")
        self.assertEqual(emp.department, "IT")
        self.assertEqual(emp.designation, "Developer")
        self.assertEqual(emp.gross_salary, 3600000)
        self.assertEqual(emp.tax, 5)
        self.assertEqual(emp.bonus, 10000)
        self.assertEqual(emp.emp_id, employee_id)

        expected_net_salary = 3600000 - (3600000 * 5 / 100) + 10000
        self.assertEqual(emp.net_salary, expected_net_salary)

    
    def test_employee_creation_without_id(self):
        emp = Employee("Deva", "HR", "Manager", 2000000, 10, 20000)
        self.assertIsInstance(emp.emp_id, str)
        self.assertEqual(len(emp.emp_id), 36)  

    def test_write_to_dict(self):
        emp = Employee("Neha", "Finance", "Analyst", 1500000, 8, 15000)
        emp_dict = emp.write_to_dict()

        self.assertEqual(emp_dict["Name"], "Neha")
        self.assertEqual(emp_dict["Department"], "Finance")
        self.assertEqual(emp_dict["Designation"], "Analyst")
        self.assertEqual(emp_dict["Gross_Salary"], 1500000)
        self.assertEqual(emp_dict["Tax"], 8)
        self.assertEqual(emp_dict["Bonus"], 15000)
        self.assertEqual(emp_dict["Net_Salary"], emp.net_salary)
        self.assertEqual(emp_dict["Employee ID"], emp.emp_id)

    def test_from_dict(self):
        data = {
            "Name": "Hema",
            "Department": "HR",
            "Designation": "Manager",
            "Gross_Salary": 1800000,
            "Tax": 6,
            "Bonus": 12000,
            "Employee ID": str(uuid.uuid4())
        }

        emp = Employee.from_dict(data)
        self.assertEqual(emp.name, data["Name"])
        self.assertEqual(emp.department, data["Department"])
        self.assertEqual(emp.designation, data["Designation"])
        self.assertEqual(emp.gross_salary, data["Gross_Salary"])
        self.assertEqual(emp.tax, data["Tax"])
        self.assertEqual(emp.bonus, data["Bonus"])
        self.assertEqual(emp.emp_id, data["Employee ID"])

    def test_string_repr(self):
        emp = Employee("Dinu", "Operations", "Manager", 1000000, 10, 5000)
        output = str(emp)
        self.assertIn("Employee ID", output)
        self.assertIn("Dinu", output)
        self.assertIn("Operations", output)
        self.assertIn("Manager", output)

if __name__ == '__main__':
    unittest.main()

        