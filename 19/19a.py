# coding=utf-8
"""Advent of Code 2015, Day 19, Part 1"""

import collections


def get_new_molecules(string, position, replacements):
    """
    Calculates the possible new molecules that can be generated for characters at a certain position in the input.
    :param string: the input string to consider
    :param position: the position at which to perform the replacements
    :param replacements: all possible replacements that can occur
    :return: the set of possible new strings following replacement
    """
    results = set()
    for replacement in replacements:
        source = string[i:i + len(replacement)]
        if source == replacement:
            for output in replacements[replacement]:
                results.add(string[:position] + output + string[position + len(replacement):])
    return results


replacements = collections.defaultdict(list)
molecules = set()

with open("input.txt") as f:
    input_list = f.read().splitlines()
for input_line in input_list[:-2]:
    from_molecule, to_molecule = input_line.split(" => ")
    replacements[from_molecule].append(to_molecule)
input_string = input_list[-1]

for i in range(len(input_string)):
    for new_molecule in get_new_molecules(input_string, i, replacements):
        molecules.add(new_molecule)

print(len(molecules))
