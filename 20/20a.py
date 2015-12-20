# coding=utf-8
"""Advent of Code 2015, Day 20, Part 1"""

import itertools


def get_factors(n):
    # noinspection LongLine,PyPep8
    """
    Calculate the factors of a number.
    Source: http://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python
    :param n: the number for which to find factors
    :return: all factors of the input number
    """
    return set(itertools.chain.from_iterable((i, n // i) for i in range(1, int(n ** 0.5) + 1) if n % i == 0))


with open("input.txt") as f:
    target = int(f.read())

"""
The house which receives the most presents most quickly will have as many factors as possible. Therefore it will be
divisible by 2, 3, 4, 5, ... and so we choose to only look at house numbers 60, 120, 180, ...
"""
house = 0
num_presents = 0
while num_presents <= target:
    house += 60
    num_presents = sum([10 * i for i in get_factors(house)])

print(house)
