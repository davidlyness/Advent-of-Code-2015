# coding=utf-8
"""Advent of Code 2015, Day 17, Part 1"""


def get_combination_count(containers, capacity):
    """
    Calculate the number of container combinations that exactly total the required capacity.
    :param containers: list of container sizes to consider
    :param capacity: required capacity
    :return: number of container combinations that total to this capacity
    """
    capacities = [1] + [0] * capacity
    for current_container in containers:
        for next_container in range(capacity, current_container - 1, -1):
            capacities[next_container] += capacities[next_container - current_container]
    return capacities[capacity]


container_list = []
total_capacity = 150

with open("input.txt") as f:
    input_list = f.read().splitlines()
for line in input_list:
    container_list.append(int(line))

print(get_combination_count(container_list, total_capacity))
