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
profitable_days= []
unprofitable_days= []


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
    elif day_pnl > minimum:
        maximum= day_pnl


    # @TODO: Write logic to determine profitable vs. unprofitable days
    if day_pnl>0:
        profitable_days.append(day_pnl)
    if day_pnl<=0:
        unprofitable_days.append(day_pnl)


# @TODO: Calculate the average
average= round (total/count, 2)

# @TODO: Calculate count metrics
Number of total trading days= len (trading_pnl)
print ("Number of total days:" Number of total trading days)

Total profits and losses= sum (day_pnl)
print ("Total Profits/Losses:" Total profits and losses)

Daily average profit and loss= (Total profits and losses )/Number of total trading days
print ("Daily Average:" Daily average profit and loss)

Worst loss= min (unprofitable_days)
print ("Worst Loss:" Worst Loss)

Best gain= max (profitable_days)

Number of profitable days= sum (day_pnl> 0)

Number of unprofitable days= sum (day_pnl<= 0)


# @TODO: Calculate percentage metrics
Percentage of profitable days= (Number of profitable days/count)*100

Percentage of unprofitable days= (Number of profitable days/count)*100


# @TODO: Print out the summary statistics
Print the values of only profitable days.
print (profitable_days)

Print the values of only unprofitable days.
print (unprofitable_days)