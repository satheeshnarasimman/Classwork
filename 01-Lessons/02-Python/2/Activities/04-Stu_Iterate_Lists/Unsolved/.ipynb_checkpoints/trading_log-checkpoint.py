# -*- coding: utf-8 -*-
"""
Student Do: Trading Log.

This script demonstrates how to perform basic analysis of trading profits/losses
over the course of a month (20 business days).
"""

# @TODO: Initialize the metric variables
count = 0
total = 0
average = 0
minimum = 0
maximum = 0


# @TODO: Initialize lists to hold profitable and unprofitable day profits/losses
profitable_day= []
unprofitable_day= []


# List of trading profits/losses
trading_pnl = [ -224,  352, 252, 354, -544,
                -650,   56, 123, -43,  254,
                 325, -123,  47, 321,  123,
                 133, -151, 613, 232, -311 ]

# @TODO: Iterate over each element of the list
for day_pnl in trading_pnl

    # @TODO: Cumulatively sum up the total and count
    total += day_pnl
    count += 1


    # @TODO: Write logic to determine minimum and maximum values
    if minimum == 0:
        minimum= day_pnl
    elif day_pnl < minimum:
        minimum= day_pnl
    elif day_pnl < minimum:
        maximum= day_pnl



    # @TODO: Write logic to determine profitable vs. unprofitable days





# @TODO: Calculate the average
average= round (total/count, 2)

# @TODO: Calculate count metrics


# @TODO: Calculate percentage metrics



# @TODO: Print out the summary statistics

