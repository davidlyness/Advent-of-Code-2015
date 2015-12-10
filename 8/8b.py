# coding=utf-8
"""Advent of Code 2015, Day 8, Part 2"""


def escape_string(nice_string):
    """
    Inserts appropriate escape characters into a string.
    :param nice_string: string into which to insert characters
    :return: string including escaped characters
    """
    escaped_str = ''
    for c in nice_string:
        if c == '"':
            escaped_str += "\\\""
        elif c == '\\':
            escaped_str += "\\\\"
        else:
            escaped_str += c
    return '"' + escaped_str + '"'


with open("input.txt") as f:
    raw_strings = f.read().splitlines()

total_length_old_code = 0
total_length_new_code = 0

for raw_string in raw_strings:
    total_length_old_code += len(raw_string)
    total_length_new_code += len(escape_string(raw_string))

print(total_length_new_code - total_length_old_code)
