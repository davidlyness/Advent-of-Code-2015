# coding=utf-8
"""Advent of Code 2015, Day 1"""

current_floor = 0
current_position = 1
first_basement = None

with open("input.txt") as f:
    for char in f.read():
        if char == "(":
            current_floor += 1
        elif char == ")":
            current_floor -= 1
        if current_floor < 0 and first_basement is None:
            first_basement = current_position
        current_position += 1

print(current_floor)
print(first_basement)
