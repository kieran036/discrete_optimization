#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created: 2021/03/08
# Author: Kieran Patel

# Marked /60

from collections import namedtuple
import numpy as np
from collections import deque
import heapq
import queue

Item = namedtuple("Item", ['index', 'value', 'weight'])
Solution = namedtuple("Solution", ['assignment', 'obj'])

file_location = r"C:\Users\patel.k.2\OneDrive - Procter and " \
                r"Gamble\PyCharm_learning\Coursera\discrete_optimization\assignments\02 knapsack\data\ks_19_0 "
with open(file_location, 'r') as input_data_file:
    input_data = input_data_file.read()
    input_data_file.close()

# parse the input, initialising items list and  determining item_count and capacity.
lines = input_data.split('\n')

firstLine = lines[0].split()
item_count = int(firstLine[0])
capacity = int(firstLine[1])
items = [0] * item_count

for i in range(0, item_count):
    line = lines[i]
    parts = line.split()
    items[i] = (Item(i, int(parts[0]), int(parts[1])))


### define the domains of all the variables {0,1}
### domains = [range(0, 2)] * item_count
### Item = namedtuple("Item", ['index', 'value', 'weight', 'level', 'bound', 'contains'])
# depth-first search algorithm implemented


# _______________________________________________________________________________

class Node:
    def __init__(self, level, value, weight, bound, contains):
        self.level = level
        self.value = value
        self.weight = weight
        self.bound = bound
        self.contains = contains


# upper_bound function only called for root node and recalculated if item not chosen
def upper_bound(node_, values_, weights_):
    # fill knapsack with fraction of first node's value as there's space and at least one item available
    if node_.weight > capacity and item_count >= 1:
        value_per_weight_node = (values_[node_.level] / weights_[node_.level])
        bound = capacity * value_per_weight_node
        return bound
    else:
        bound = node_.value
        weight_unbroken_items = node_.weight
        next_node_lvl = node_.level + 1

        # fill knapsack with unbroken items until whole pieces can no longer fit
        if next_node_lvl <= item_count:
            while weight_unbroken_items + weights_[next_node_lvl] <= capacity:
                bound += values_[next_node_lvl]
                weight_unbroken_items += weights_[next_node_lvl]
                next_node_lvl += 1

            # fill knapsack with fraction of the last node's value as there's space for a fraction
            if weight_unbroken_items + weights_[next_node_lvl] > capacity:
                value_per_weight_next_node = (values_[next_node_lvl] / weights_[next_node_lvl])
                bound += (capacity - weight_unbroken_items) * value_per_weight_next_node
            else:
                return bound
        else:
            return bound


def knapsack(items_):
    # sort items by value to weight ratio
    sorted_items = sorted(items, key=lambda k: float(k.value) / k.weight, reverse=True)

    list_of_values = [0] * item_count
    list_of_weights = [0] * item_count

    for x, item in enumerate(sorted_items, 0):
        list_of_values[x] = int(item.value)
        list_of_weights[x] = int(item.weight)

    root_node = Node(level=0, value=0, weight=0, bound=0.0, contains=[])
    root_node.bound = upper_bound(root_node, list_of_values, list_of_weights)
    q = queue.Queue()
    q.put(root_node)

# TODO: Complete BFS from this line onwards and then perform DFS

    # initialise taken list which determines if the item is chosen and the set for nodes to be inserted into
    taken = [0] * item_count
    best = set()
    value = 0

    while not q.empty():
        fifo_node = q.get()
        if fifo_node.bound > value:
            level = fifo_node.level + 1
        # check 'left' node (if item is added to knapsack)

        left = Node(level, fifo_node.value + list_of_values[level - 1], fifo_node.weight + list_of_weights[level - 1],
                    0.0,
                    fifo_node.contains[:])
        left.bound = upper_bound(left, list_of_values, list_of_weights)
        left.contains.append(level)
        if left.weight <= capacity:
            if left.value > value:
                value = left.value
                best = set(left.contains)
            if left.bound > value:
                q.put(left)
            # check 'right' node (if items is not added to knapsack)
        right = Node(level, fifo_node.value, fifo_node.weight, 0.0, fifo_node.contains[:])
        right.bound = upper_bound(right, list_of_values, list_of_weights)
        if right.weight <= capacity:
            if right.value > value:
                value = right.value
                best = set(right.contains)
            if right.bound > value:
                q.put(right)
    for b in best:
        taken[b - 1] = 1
    value = sum([i * j for (i, j) in zip(list_of_values, taken)])
    return str(value), taken






# prepare the solution in the specified output format
output_data = str(value) + ' ' + str(0) + '\n'
output_data += ' '.join(map(str, taken))
print(output_data)
