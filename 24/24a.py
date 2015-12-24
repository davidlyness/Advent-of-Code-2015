# coding=utf-8
"""Advent of Code 2015, Day 24, Part 1"""

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


def calculate_optimal_groupings(packages):
    """
    Calculates the optimal groupings for a given set of packages.
    :param packages: reference set of packages to group
    :return: QE value of optimal arrangement
    """
    required_group_weight = sum(packages) / 3
    length_group_1 = 1
    while length_group_1 < len(packages):
        for combo_group_1 in itertools.combinations(packages, length_group_1):
            if sum(combo_group_1) == required_group_weight:
                remaining_packages_two = packages - set(combo_group_1)
                for length_group_2 in range(len(remaining_packages_two)):
                    for combo_group_2 in itertools.combinations(remaining_packages_two, length_group_2):
                        if sum(combo_group_2) == required_group_weight:
                            combo_group_3 = remaining_packages_two - set(combo_group_2)
                            if sum(combo_group_3) == required_group_weight:
                                return qe(combo_group_1)
        length_group_1 += 1
    return -1

with open("input.txt") as f:
    package_set = set([int(x) for x in f.read().splitlines()])

print(calculate_optimal_groupings(package_set))
