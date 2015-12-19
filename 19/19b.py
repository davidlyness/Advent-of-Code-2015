# coding=utf-8
"""Advent of Code 2015, Day 19, Part 2"""

import collections


def get_source_molecules(string, position, replacements):
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


reverse_replacements = collections.defaultdict(list)
molecules = set()

with open("input.txt") as f:
    input_list = f.read().splitlines()
for input_line in input_list[:-2]:
    from_molecule, to_molecule = input_line.split(" => ")
    reverse_replacements[to_molecule].append(from_molecule)
target_string = input_list[-1]

created_molecules = set()
created_molecules.add(target_string)
steps = 0

"""
Strategy
========
Part 1: Building up the long-length molecule starting from 'e' will take way too long. Instead we'll start with the
target molecule and work backwards, generating shorter and shorter molecules until we hit 'e'.

Part 2: It turns out this also takes way too long - there are too many possible combinations to backtrack through. Given
a heuristic of "at each stage on the correct path, we're probably reducing the size of the input string by a large
amount", we keep only the 10 shortest strings at each step. Increasing this number will increase the chance of hitting
on the correct answer, but will incur a performance hit. (Currently takes < 5 seconds to find the answer.)
"""

while "e" not in created_molecules:
    previous_molecules = set()
    for molecule in created_molecules:
        for i in range(len(molecule)):
            for new_molecule in get_source_molecules(molecule, i, reverse_replacements):
                previous_molecules.add(new_molecule)
    # This is where we limit ourselves to only the "top" 10 results of each iteration, by shortest length.
    created_molecules = set(sorted(list(previous_molecules), key=len)[:10])
    steps += 1

print(steps)
