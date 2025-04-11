'''
Author :- Ponnulekshmi P 
UID :- 249474
Date :- 11/04/2025
Description:-   Python file for Employee Management System storage operations.

'''

import pickle
import os

# Class for storage creation
class Storage(object):

    def __init__(self, filename='employee.pkl'):
        self.filename = filename

# To save into pickle file
    def save(self, emp_list):
        with open(self.filename, 'wb') as file:
            pickle.dump(emp_list, file)

# To load data from pickel file
    def load(self):
        if not os.path.exists(self.filename):
            return []  

        with open(self.filename, "rb") as file:
            return pickle.load(file)