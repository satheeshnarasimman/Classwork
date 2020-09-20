# -*- coding: utf-8 -*-
"""Student Do: E-Commerce Traffic.

This script will parse through a text file and sum the total
number of customers and the count of days in the text file to
calculate the daily average of customer traffic for an e-commerce
business.
"""

# @TODO: From the pathlib library, import the main class Path
from pathlib import Path

# @TODO: Check the current directory where the Python program is executing from
current_path= Path.cwd()
print (f"currently in {current_path}")

# @TODO: Set the path using Pathlib
file_path= Path("../Resources/customer_traffic.txt")

# Initialize variables
customer_total = 0
day_count = 0

# @TODO: Open the file in "read" mode ('r') and store the contents in the variable 'file'
with open (file_path, 'r') as file:

    # @TODO: Parse the file line by line
    for line in file:

        # @TODO: Convert the number in the text file from string to int (allows for numerical calculations)
        number= int (line)

        # @TODO: Sum the total and count of the numbers in the text file



# @TODO: Print out customer_total and day_count




# @TODO: Calculate the average



# @TODO: Set output file name


# @TODO: Open the output path as a file object

    # @TODO: Write daily_average to the output file, convert to string
