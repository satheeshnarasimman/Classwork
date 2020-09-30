# @TODO: Your code here

import csv
from pathlib import Path

filepath= Path('../Resources/employees.csv')

new_employee_data= []

# Read into dictionary and create a new email field

with open (filepath) as file:
    reader= csv.Dictreader(file)
    for row in reader:
        first_name= row['first_name']
        last_name= row['last_name']
        
    # @ TODO Generate email address
    email= first_name + '.' + last_name + '@example.com'
    
    new_employee_data.append (
     {'first_name': row['first_name']
      'last_name': row['last_name']
        'ssn': row['ssn']
        'email': email}
    )