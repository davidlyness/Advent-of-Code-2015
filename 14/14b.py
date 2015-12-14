# coding=utf-8
"""Advent of Code 2015, Day 14, Part 2"""

import collections
import re

with open("input.txt") as f:
    input_list = f.read().splitlines()

stats = collections.defaultdict(dict)
race = collections.defaultdict(dict)

for line in input_list:
    p = re.compile("(.*) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.")
    match = p.match(line).groups()
    stats[match[0]]['fly_speed'] = int(match[1])
    stats[match[0]]['fly_length'] = int(match[2])
    stats[match[0]]['rest_length'] = int(match[3])

total_time = 2503
lead_position = 0

for reindeer in stats:
    race[reindeer]['position'] = 0
    race[reindeer]['points'] = 0
    race[reindeer]['speed'] = stats[reindeer]['fly_speed']
    race[reindeer]['remaining_time'] = stats[reindeer]['fly_length']

for _ in range(total_time):
    for reindeer in race:
        race[reindeer]['remaining_time'] -= 1
        race[reindeer]['position'] += race[reindeer]['speed']
        if race[reindeer]['remaining_time'] == 0:
            if race[reindeer]['speed'] == 0:
                race[reindeer]['speed'] = stats[reindeer]['fly_speed']
                race[reindeer]['remaining_time'] = stats[reindeer]['fly_length']
            else:
                race[reindeer]['speed'] = 0
                race[reindeer]['remaining_time'] = stats[reindeer]['rest_length']
    lead_position = max([race[reindeer]['position'] for reindeer in race])
    for reindeer in race:
        if race[reindeer]['position'] == lead_position:
            race[reindeer]['points'] += 1

print(max([race[reindeer]['points'] for reindeer in race]))
