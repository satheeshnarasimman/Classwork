# -*- coding: utf-8 -*-
"""Student Activity: Financial Analysis using NPV.

This script will choose the optimal project scenario to
undertake based on max NPV values.
"""

# @TODO: Import the NumPy Financial (numpy_financial) library


# Discount Rate
discount_rate = .1

# Initial Investment, Cash Flow 1, Cash Flow 2, Cash Flow 3, Cash Flow 4
cash_flows_conservative = [-1000, 400, 400, 400, 400]
cash_flows_neutral = [-1500, 600, 600, 600, 600]
cash_flows_aggressive = [-2250, 800, 800, 800, 800]

# @TODO: Initialize dictionary to hold NPV return values
npv_dict = {}

# @TODO: Calculate the NPV for each scenario
npv_dict['conservative']= npf.npv(discount_rate, cash_flows_conservative)
npv_dict['neutral']= npf.npv(discount_rate, cash_flows_neutral)
npv_dict['aggressive']= npf.npv(discount_rate, cash_flows_aggressive)



# @TODO: Initialize variables
max_npv= 0
max_discount_rates= 0

# @TODO: Iterate over npv_dict to find the max key-value pair
for discount_rates, cash_flows in npv_dict.items:
    if max_npv == 0:
        max_npv= cash_flows
        max_discount_rates= discount_rates
    elif cash_flows> max_npv:
        max_npv= cash_flows
        max_discount_rates= discount_rates
        

# @TODO: Print out the optimal project scenario with the highest NPV value
print (f"The project scenario with the max NPV value is {max_discount_rates} with a NPV of {max_npv}")