#!/usr/bin/python
# -*- coding: utf-8 -*-


from collections import namedtuple

import numpy as np

Item = namedtuple("Item", ['index', 'value', 'weight'])


def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])
    items = []

    for i in range(1, item_count + 1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i - 1, int(parts[0]), int(parts[1])))

    # dynamic programming algorithm implemented
    # transposed to order i and j such that it's more readable
    # added = [[0] * (capacity + 1) for i in range(item_count + 1)]
    np_table = np.zeros((capacity + 1, item_count + 1), dtype='int').transpose()  # 11+1, 4+1
    for i in range(item_count + 1):
        for j in range(capacity + 1):
            if i == 0 or j == 0:
                np_table[i][j] = 0
            elif items[i - 1].weight <= j:
                np_table[i][j] = max(np_table[i - 1][j], items[i - 1].value + np_table[i - 1][j - items[i - 1].weight])
            else:
                np_table[i][j] = np_table[i - 1][j]

    # optimal value
    np_table = np_table.transpose()
    value = np_table[capacity][item_count]
    # print(value)
    # print(np_table)

    # You essentially look at if O(k, j - 1) != O(k, j) is True. If it is, you move to it and subtract the weight from
    # that item, since it was chosen, else you just keep following up. This is done until the knapsacks capacity is
    # exhausted == 0. traceback to find soln
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

    # prepare the solution in the specified output format
    output_data = str(value) + ' ' + str(1) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py '
              './data/ks_4_0)')
