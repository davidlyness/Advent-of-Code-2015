# coding=utf-8
"""Advent of Code 2015, Day 12, Part 1"""

import json


def calculate_total(data):
    """
    Recursively calculates the total for each element of JSON data.
    :param data: JSON data for which to calculate the total
    :return: total for the provided JSON data
    """
    total = 0
    if isinstance(data, int):
        total += data
    elif isinstance(data, str):
        pass
    elif isinstance(data, list):
        total += sum(calculate_total(x) for x in data)
    else:
        for item in data:
            total += calculate_total(item)
            total += calculate_total(data[item])
    return total


with open("input.txt") as f:
    json_string = f.read()[:-1]

json_data = json.loads(json_string)
print(calculate_total(json_data))
