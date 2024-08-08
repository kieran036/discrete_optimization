#!/usr/bin/python
# -*- coding: utf-8 -*-
# Marked /60

from collections import namedtuple
import numpy as np
from collections import deque
import heapq
import queue

Item = namedtuple("Item", ['index', 'value', 'weight'])


file_location = r"C:\Users\patel.k.2\OneDrive - Procter and " \
                r"Gamble\PyCharm_projects\Coursera\discrete_optimization\assignments\02 knapsack\data\ks_19_0 "
with open(file_location, 'r') as input_data_file:
    input_data = input_data_file.read()

# COMMENT
# parse the input
lines = input_data.split('\n')

firstLine = lines[0].split()
item_count = int(firstLine[0])
capacity = int(firstLine[1])

items = []
optimistic_estimate = 0

for i in range(1, item_count + 1):
    line = lines[i]
    parts = line.split()
    items.append(Item(i - 1, int(parts[0]), int(parts[1])))
    optimistic_estimate += + int(parts[1])








    from collections import namedtuple

    Problem = namedtuple("Problem", ['items', 'sets'])
    Set = namedtuple("Set", ['index', 'cost', 'items'])
    Solution = namedtuple("Solution", ['assignment', 'obj'])


    def solve_it(input_data):

        # parse the input
        lines = input_data.split('\n')

        parts = lines[0].split()
        item_count = int(parts[0])
        set_count = int(parts[1])

    sets = []
    for i in range(1, set_count + 1):
        parts = lines[i].split()
        sets.append(Set(i - 1, float(parts[0]), map(int, parts[1:])))

    problem = Problem(range(0, item_count), sets)

    # define the domains of all the variables {0,1}
    domains = [range(0, 2)] * set_count

    # start a trivial depth first search for a solution
    solution = tryall([], domains, problem)

    # prepare the solution in the specified output format
    output_data = str(solution.obj) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, solution.assignment))

    return output_data


def tryall(assignment, domains, problem):
    # base-case: if the domains list is empty, all values are assigned
    # check if it is a solution, return None if it is not
    if len(domains) == 0:
        obj = check_it(assignment, problem)
        if obj != None:
            return Solution(assignment, obj)
        else:
            return None

    # recursive-case: try each value in the next domain
    # if we find a solution return it. otherwise, try the next value
    else:
        best_sol = None
        for v in domains[0]:
            sol = tryall(assignment[:] + [v], domains[1:], problem)
            if sol != None:
                if best_sol == None or best_sol.obj > sol.obj:
                    best_sol = sol
        return best_sol


































































# COMMENT
# add densities to col index -1
np_items = np.array(items, dtype=float)
densities = np.divide([np_items[:, 2]], [np_items[:, 1]], dtype=float).transpose()
np_items = np.hstack((np_items, densities))
np_items = np_items[item_count + 1 - np_items[:, -1].argsort()]

# depth-first search algorithm implemented
value = 0
weight = 0

### optimistic_estimate
### capacity
### taken = [0] * len(items)






# COMMENT
# prepare the solution in the specified output format
output_data = str(value) + ' ' + str(0) + '\n'
output_data += ' '.join(map(str, taken))
print(output_data)
