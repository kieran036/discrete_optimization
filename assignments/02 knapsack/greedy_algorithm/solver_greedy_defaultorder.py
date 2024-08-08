# !/usr/bin/python
# Created: 2021/03/04
# Author: Kieran Patel
# -*- coding: utf-8 -*-

# Marked 3/10 for all 6 submitted problems.

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
value = 0
weight = 0
taken = [0] * len(items)

for item in items:
    if item.value > 0 and weight + item.weight <= capacity:
        taken[item.index] = 1
        value += item.value
        weight += item.weight

# Prepare the solution in the specified output format
output_data = str(value) + ' ' + str(0) + '\n'
output_data += ' '.join(map(str, taken))
print(output_data)
