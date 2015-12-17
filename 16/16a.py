# coding=utf-8
"""Advent of Code 2015, Day 16, Part 1"""

import collections
import re

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
    if all(sues[sue][prop] == reqs[prop] for prop in sues[sue]):
        gifter = sue

print(gifter)
