#!/usr/bin/python
# -*- coding: utf-8 -*-
# Marked /60

from collections import namedtuple
import numpy as np
from collections import deque
import heapq
import queue
import math

Item = namedtuple("Item", ['index', 'value', 'weight'])
Solution = namedtuple("Solution", ['assignment', 'obj'])

file_location = r"C:\Users\patel.k.2\OneDrive - Procter and " \
                r"Gamble\PyCharm_learning\Coursera\discrete_optimization\takens\02 knapsack\data\ks_19_0 "
with open(file_location, 'r') as input_data_file:
    input_data = input_data_file.read()
    input_data_file.close()

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

# COMMENT
# add densities to col index -1
np_items = np.array(items, dtype=float)
densities = np.divide([np_items[:, 2]], [np_items[:, 1]], dtype=float).transpose()
np_items = np.hstack((np_items, densities))
np_items = np_items[item_count + 1 - np_items[:, -1].argsort()]

# define the domains of all the variables {0,1}
domains = [range(0, 2)] * item_count
### domains = np.array([range(0, 2)] * item_count)
# depth-first search algorithm implemented
value = 0
capacity
optimistic_estimate
taken = [] * item_count
best = set()










import queue
from collections import namedtuple
Item = namedtuple("Item", ['index', 'value', 'weight', 'level', 'bound', 'contains'])

class Node:
    def __init__(self, level, value, weight, bound, contains):
         self.level = level
         self.value = value
         self.weight = weight
         self.bound = bound
         self.contains = contains

# Only calculated at start and recalculated if item not chosen
def upper_bound(node_, capacity_, item_count_, values_, weights_):
    if node_.weight > capacity_:
        return 0
    else:
        bound = node_.value
        wt = node_.weight
        next_node_lvl = node_.level + 1
        while next_node_lvl < item_count_ and wt + weights_[j] <= capacity_:
            bound += values_[next_node_lvl]
            wt += weights_[next_node_lvl]
            next_node_lvl += 1
    # fill knapsack with fraction of a remaining item
            if next_node_lvl < item_count_:
                bound += (capacity_ - wt) * (values_[next_node_lvl] / weights_[next_node_lvl])
#                 bound += values_[next_node_lvl]
            return bound

root = Node(0, 0, 0, 0.0,[])


def knapsack(items_, capacity_):
    values = [0] * item_count
    weights = [0] * item_count
    # sort items by value to weight ratio
    items = sorted(items, key=lambda k: float(k.value) / k.weight, reverse=True)
    for i, item in enumerate(items, 0):
        values[i] = int(item.value)
        weights[i] = int(item.weight)
    q = Queue.Queue()
    root = Node(0, 0, 0, 0.0, [])
    root.bound = upper_bound(root, capacity, item_count, v, weights)
    q.put(root)
    value = 0
    taken = [0] * item_count
    best = set()
    while not q.empty():
        c = q.get()
        if c.bound > value:
            level = c.level + 1
        # check 'left' node (if item is added to knapsack)
        left = Node(level, c.value + values[level - 1], c.weight + weights[level - 1], 0.0, c.contains[:])
        left.bound = upper_bound(left, capacity, item_count, values, weights)
        left.contains.append(level)
        if left.weight <= capacity:
            if left.value > value:
                value = left.value
                best = set(left.contains)
            if left.bound > value:
                q.put(left)
            # check 'right' node (if items is not added to knapsack)
        right = Node(level, c.value, c.weight, 0.0, c.contains[:])
        right.bound = upper_bound(right, capacity, item_count, v, weights)
        if right.weight <= capacity:
            if right.value > value:
                value = right.value
                best = set(right.contains)
            if right.bound > value:
                q.put(right)
    for b in best:
        taken[b - 1] = 1
    value = sum([i * j for (i, j) in zip(v, taken)])
    return str(value)




















def upper_bound(u, k, n, v, w):
    if u.weight > k:
        return 0

    else:
        bound = u.value
        wt = u.weight
        j = u.level + 1

        while j < n and wt + w[j] <= k:
            bound += v[j]
            wt += w[j]
            j += 1

    # fill knapsack with fraction of a remaining item
            if j < n:
                bound += (k - wt) * (v[j] / w[j])

            return bound











# start a trivial depth first search for a solution
solution = tryall([], domains, problem)


def tryall(taken, domains, problem):
    # base-case: if the domains list is empty, all values are assigned
    # check if it is a solution, return None if it is not
    if len(domains) == 0:
        # # obj = check_it(taken, problem)
        # if obj != None:
        #     return Solution(taken, obj)
        # else:
        #     return None

    # recursive-case: try each value in the next domain
    # if we find a solution return it. otherwise, try the next value
    else:
        best_sol = None
        for v in domains[0]:
            sol = tryall(taken[:] + [v], domains[1:], problem)
            if sol != None:
                if best_sol == None or best_sol.obj > sol.obj:
                    best_sol = sol
        return best_sol



# when first node chosen then
# for i in range(item_count):
    value += np_items[i][1]
    capacity -= np_items[i][2]
#    optimistic_estimate = unchanged



for i in range(item_count):
    for j in range(item_count):
        for k in range(item_count):

### taken = [0] * len(items)






# COMMENT
# prepare the solution in the specified output format
output_data = str(value) + ' ' + str(0) + '\n'
output_data += ' '.join(map(str, taken))
print(output_data)
