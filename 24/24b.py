# coding=utf-8
"""Advent of Code 2015, Day 24, Part 2"""

import itertools


def qe(group):
    """
    Calculates the QE (product) of a group. Because product(n) doesn't exist... :(
    :param group: the reference group
    :return: the QE of a group
    """
    p = 1
    for n in group:
        p *= n
    return p


with open("input.txt") as f:
    packages = set([int(x) for x in f.read().splitlines()])

required_group_weight = sum(packages) / 4
best_qe = None
length_group_1 = 1

while best_qe is None and length_group_1 < len(packages):
    for combo_group_1 in itertools.combinations(packages, length_group_1):
        if sum(combo_group_1) == required_group_weight:
            remaining_packages_two = packages - set(combo_group_1)
            for length_group_2 in range(len(remaining_packages_two)):
                for combo_group_2 in itertools.combinations(remaining_packages_two, length_group_2):
                    if sum(combo_group_2) == required_group_weight:
                        remaining_packages_three = remaining_packages_two - set(combo_group_2)
                        for length_group_3 in range(len(remaining_packages_three)):
                            for group_combo_3 in itertools.combinations(remaining_packages_three, length_group_3):
                                if sum(group_combo_3) == required_group_weight:
                                    group_combo_4 = remaining_packages_three - set(group_combo_3)
                                    if sum(group_combo_4) == required_group_weight:
                                        current_qe = qe(combo_group_1)
                                        if best_qe is None or current_qe < best_qe:
                                            best_qe = current_qe
    length_group_1 += 1

print(best_qe)
