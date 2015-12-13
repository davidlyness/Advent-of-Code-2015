# coding=utf-8
"""Advent of Code 2015, Day 13, Part 2"""

import collections
import itertools
import re

with open("input.txt") as f:
    input_list = f.read().splitlines()

happiness = collections.defaultdict(dict)
best_happiness = None

for line in input_list:
    p = re.compile("(.*) would (.*) (\d+) happiness units by sitting next to (.*)\.")
    match = p.match(line).groups()
    if match[1] == "gain":
        happiness_change = int(match[2])
    else:
        happiness_change = -int(match[2])
    happiness[match[0]][match[3]] = happiness_change

for person in list(happiness):
    happiness["Me"][person] = 0
    happiness[person]["Me"] = 0

for arrangement in itertools.permutations(happiness.keys()):
    happiness_change = sum(happiness[i][j] + happiness[j][i] for i, j in zip(arrangement, arrangement[1:]))
    happiness_change += happiness[arrangement[0]][arrangement[-1]] + happiness[arrangement[-1]][arrangement[0]]
    if best_happiness is None or happiness_change > best_happiness:
        best_happiness = happiness_change

print(best_happiness)
