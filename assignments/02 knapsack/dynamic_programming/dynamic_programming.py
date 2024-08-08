# !/usr/bin/python
# -*- coding: utf-8 -*-
# Created: 2021/03/06
# Author: Kieran Patel

# Computes a table to store all the possible values for each capacity up to
# full capacity and for each variable. We look at the column to the left and decide if we take the left value or if
# we accept the value for the current column in which case we will have the value of the item in the current column
# plus the value for the weight with the weight of the value removed and one less item Marked 10/10 for first 3
# problems and remaining were computationally too long to submit.

from collections import namedtuple
import numpy as np

Item = namedtuple("Item", ['index', 'value', 'weight'])

file_location = r"C:\Users\patel.k.2\OneDrive - Procter and " \
                r"Gamble\PyCharm_learning\Coursera\discrete_optimization\assignments\02 knapsack\data\ks_19_0 "
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

# Dynamic programming algorithm implemented
# Transposed to order i and j such that it's more readable
np_table = np.zeros((capacity + 1, item_count + 1), dtype='int').transpose()
for i in range(item_count + 1):
    for j in range(capacity + 1):
        if i == 0 or j == 0:
            np_table[i][j] = 0
        elif items[i - 1].weight <= j:
            np_table[i][j] = max(np_table[i - 1][j], items[i - 1].value + np_table[i - 1][j - items[i - 1].weight])
        else:
            np_table[i][j] = np_table[i - 1][j]

# Optimal value
np_table = np_table.transpose()
value = np_table[capacity][item_count]

# Check if O(k, j - 1) != O(k, j) is True. If it is, you move to it and subtract the weight from that item, since
# it was chosen, else you just keep following up. This is done until the knapsacks capacity is exhausted == 0. Below
# is the traceback to find soln
i = capacity
j = item_count
taken = [0] * item_count
optimal_value = np_table[i][j]
while i > 0 and j >= 0:
    if np_table[i][j] == np_table[i][j - 1]:
        j -= 1
    if np_table[i][j] != np_table[i][j - 1]:
        taken[j - 1] = 1
        i -= items[j - 1].weight

# Prepare the solution in the specified output format
output_data = str(value) + ' ' + str(0) + '\n'
output_data += ' '.join(map(str, taken))
print(output_data)
