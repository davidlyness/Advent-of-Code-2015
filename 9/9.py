# coding=utf-8
"""Advent of Code 2015, Day 9"""

import collections
import itertools

with open("input.txt") as f:
    raw_strings = f.read().splitlines()

routes = collections.defaultdict(dict)

for raw_string in raw_strings:
    route, distance = raw_string.split(" = ")
    from_city, to_city = route.split(" to ")
    routes[from_city][to_city] = int(distance)
    routes[to_city][from_city] = int(distance)

shortest_distance = None
longest_distance = None
for path in itertools.permutations(routes.keys()):
    current_distance = 0
    for from_city, to_city in zip(path, path[1:]):
        current_distance += routes[from_city][to_city]
    if shortest_distance is None or current_distance < shortest_distance:
        shortest_distance = current_distance
    if longest_distance is None or current_distance > longest_distance:
        longest_distance = current_distance

print(shortest_distance)
print(longest_distance)
