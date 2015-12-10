# coding=utf-8
"""Advent of Code 2015, Day 8, Part 1"""

with open("input.txt") as f:
    raw_strings = f.read().splitlines()

total_length_code = 0
total_length_memory = 0

for raw_string in raw_strings:
    total_length_code += len(raw_string)
    total_length_memory += len(eval(raw_string))

print(total_length_code - total_length_memory)
