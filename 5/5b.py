# coding=utf-8
"""Advent of Code 2015, Day 5, Part 2"""

import re


def is_nice_string(string):
    """
    Determines whether a string is nice.
    :param string: the candidate string to check
    :return: whether the string is nice (boolean)
    """
    return has_repeated_double_letter(string) and has_repeated_letter_with_gap(string)


def has_repeated_double_letter(string):
    """
    Determines whether a string has a repeated double letter.
    :param string: the candidate string to check
    :return: whether the string has a repeated double letter (boolean)
    """
    pattern = re.compile(".*(..).*\\1")
    return bool(pattern.match(string))


def has_repeated_letter_with_gap(string):
    """
    Determines whether a string has a repeated letter with one-character gap in between.
    :param string: the candidate string to check
    :return: whether the string has a repeated letter with one-character gap in between (boolean)
    """
    pattern = re.compile(".*(.).\\1.*")
    return bool(pattern.match(string))


with open("input.txt") as f:
    strings = f.read().splitlines()

nice_strings = []

for nice_candidate in strings:
    if is_nice_string(nice_candidate):
        nice_strings.append(nice_candidate)

print(len(nice_strings))
