# coding=utf-8
"""Advent of Code 2015, Day 16, Part 2"""

import collections
import re


def is_match(property_name, aunt_value, req_value):
    """
    Determines whether the aunt's property value is a match for the requirements.
    :param property_name: name of the property under test
    :param aunt_value: aunt's property value
    :param req_value: required property value
    :return: whether the aunt's property value meets the requirements
    """
    if property_name in ["cats", "trees"]:
        return aunt_value > req_value
    elif property_name in ["pomeranians", "goldfish"]:
        return aunt_value < req_value
    else:
        return aunt_value == req_value


sues = collections.defaultdict(dict)
reqs = dict()
gifter = None

with open("sues.txt") as f:
    input_list = f.read().splitlines()
for line in input_list:
    p = re.compile("Sue (\d+): (.*)")
    match = p.match(line).groups()
    aunt_num = int(match[0])
    properties = match[1].split(", ")
    for prop in properties:
        name, value = prop.split(": ")
        sues[aunt_num][name] = int(value)

with open("input.txt") as f:
    input_list = f.read().splitlines()
for line in input_list:
    name, value = line.split(": ")
    reqs[name] = int(value)

for sue in sues:
    if all(is_match(prop, sues[sue][prop], reqs[prop]) for prop in sues[sue]):
        gifter = sue

print(gifter)
