'''
Author :- Ponnulekshmi P 
UID :- 249474
Date :- 11/04/2025
Description:-   THE USER INTERACTIVE PYTHON FILE

'''
# Import the functions from Employeemanagement and Storage
from employee_management import Employeemanagement
from storage import Storage

def display_details(emp_details: list) -> None:
    if not emp_details:
        print("No data to display")
    else:
        for data in emp_details:
            print(f"Employee ID : {data.emp_id}, Name : {data.name}, Department : {data.department}, Designation : {data.designation}, Gross Salary : {data.gross_salary}, Tax : {data.tax}, Bonus : {data.bonus}, Net Salary : {data.net_salary}")
            

# Main  function

def main():
    
    emp_data = Employeemanagement()
    store = Storage()
    
    saved_data = store.load()
    emp_data.load_emp_details(saved_data)

    while(True):
        
        print("----------------THE EMPLOYEE MANAGEMENT SYSTEM----------------")
        print("1. ADD a new Employee")
        print("2. VIEW the Employee List")
        print("3. SEARCH for an Employee using the ID")
        print("4. DELETE an Employee data using Name")
        print("5. QUIT from the App")
        
        print("Enter your choice: ")
        choice = int(input())
        
        if choice == 1:
            name = input("Enter the name of the Employee: ")
            department = input("Enter the department of the Employee: ")
            designation = input("Enter the designation of the Employee: ")
            gross_salary = int(input("Enter the gross salary of the employee: "))
            tax = int(input("Enter the tax of the employee: "))
            bonus = int(input("Enter the bonus for the employee: "))
            
            employee = emp_data.add_employee(name, department, designation, gross_salary, tax, bonus)
            store.save(emp_data.to_dict_list())
            print(f"Employee added with ID: {employee.emp_id}")
        elif choice == 2:
            display_details(emp_data.view_details())
        elif choice == 3:
            id = input("Enter the employee ID: ")
            result = emp_data.search_by_id(id)
            if (result):
                print(result)
                store.save(emp_data.to_dict_list())
                print("Got the data!!!")
            else:
                print("Employee ID not found")
        elif choice == 4:
            name = input("Enter the Employee Name: ")
            if emp_data.delete_by_name(name):
                store.save(emp_data.to_dict_list())
                print("Deleted the data!!!")
            else:
                print(f"Employee with name {name} not found")
        elif choice == 5:
            print("User request is to QUIT")
            print("-----Closing the App-----")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":

    main()
