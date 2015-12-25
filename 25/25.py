# coding=utf-8
"""Advent of Code 2015, Day 25"""

import collections
import re


def calculate(target_row, target_column):
    """
    Calculates the number present in the specified grid position.
    :param target_row: specified row
    :param target_column: specified column
    :return: value at co-ordinate (target_row, target_column)
    """
    grid = collections.defaultdict(dict)
    grid[1][1] = 20151125
    current_row, current_column = 1, 1
    while (current_row != target_row) or (current_column != target_column):
        previous_row, previous_column = current_row, current_column
        if previous_row == 1:
            current_row, current_column = previous_column + 1, 1
        else:
            current_row, current_column = previous_row - 1, previous_column + 1
        grid[current_row][current_column] = (grid[previous_row][previous_column] * 252533) % 33554393

    return grid[target_row][target_column]


with open("input.txt") as f:
    input_string = f.read()
r = re.compile(".* row (\d+), column (\d+).")
match = r.match(input_string).groups()
row = int(match[0])
column = int(match[1])

print(calculate(row, column))
