# coding=utf-8
"""Advent of Code 2015, Day 17, Part 2"""

import itertools


def get_minimal_combination(containers, capacity):
    """
    Calculate the number of minimal container combinations that exactly total the required capacity.
    :param containers: list of container sizes to consider
    :param capacity: required capacity
    :return: number of minimal container combinations that total to this capacity
    """
    minimum_capacity_count = 0
    for container_count in range(1, len(containers) + 1):
        for combination in itertools.combinations(containers, container_count):
            if sum(combination) == capacity:
                minimum_capacity_count += 1
        if minimum_capacity_count > 0:
            break
    return minimum_capacity_count


container_list = []
total_capacity = 150

with open("input.txt") as f:
    input_list = f.read().splitlines()
for line in input_list:
    container_list.append(int(line))

print(get_minimal_combination(container_list, total_capacity))
