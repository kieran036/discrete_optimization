#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created: 2021/03/04
# Author: Kieran Patel

# Marked 29/60 between all 6 submitted problems.

from collections import namedtuple

Item = namedtuple("Item", ['index', 'value', 'weight'])

file_location = r"C:\Users\patel.k.2\OneDrive - Procter and " \
                r"Gamble\PyCharm_projects\Coursera\discrete_optimization\assignments\02 knapsack\data\ks_4_0 "
with open(file_location, 'r') as input_data_file:
    input_data = input_data_file.read()

# Parse the input
lines = input_data.split('\n')

firstLine = lines[0].split()
item_count = int(firstLine[0])
capacity = int(firstLine[1])

items = []

for i in range(1, item_count + 1):
    line = lines[i]
    parts = line.split()
    items.append(Item(i - 1, int(parts[0]), int(parts[1])))

# A trivial algorithm for filling the knapsack
# It takes items in-order until the knapsack is full
# Sorts by weight in ascending to begin filling with smallest items
items.sort(key=lambda x: x[1], reverse=True)

value = 0
weight = 0
taken = [0] * len(items)

for item in items:
    if item.value > 0 and weight + item.weight <= capacity:
        taken[item.index] = 1
        value += item.value
        weight += item.weight

# Alternative approach which combines capacity and weight into a single variable as capacity is a constant and weight
# is the variable which changes with each iteration.

# SUPPLEMENTARY CODE
# available_space = capacity
# for item in items:
#     if item.value > 0 and item.weight <= available_space:
#         taken[item.index] = 1
#         value += item.value
#         available_space -= item.weight

# This section of code supplements the above with the assumption the item can be fractional. It outputs what the value
# can be if constraints allow for fractional inputs and no binary 0 and 1.

# SUPPLEMENTARY CODE
#     else:
#         fraction_of_item = available_space / item.weight
#         value += item.value * fraction_of_item
#         available_space -= item.weight * fraction_of_item

# Prepare the solution in the specified output format
output_data = str(value) + ' ' + str(0) + '\n'
output_data += ' '.join(map(str, taken))
print(output_data)
