# coding=utf-8
"""Advent of Code 2015, Day 5, Part 1"""

import re


def is_nice_string(string):
    """
    Determines whether a string is nice.
    :param string: the candidate string to check
    :return: whether the string is nice (boolean)
    """
    return has_three_vowels(string) and has_double_letter(string) and not has_a_forbidden_substring(string)


def has_three_vowels(string):
    """
    Determines whether a string has three vowels.
    :param string: the candidate string to check
    :return: whether the string has three vowels (boolean)
    """
    pattern = re.compile(".*([aeiou].*){3,}")
    return bool(pattern.match(string))


def has_double_letter(string):
    """
    Determines whether a string has a double letter.
    :param string: the candidate string to check
    :return: whether the string has a double letter (boolean)
    """
    pattern = re.compile(".*(.)\\1.*")
    return bool(pattern.match(string))


def has_a_forbidden_substring(string):
    """
    Determines whether a string has a forbidden substring.
    :param string: the candidate string to check
    :return: whether the string has a forbidden substring (boolean)
    """
    return any(forbidden_string in string for forbidden_string in ["ab", "cd", "pq", "xy"])


with open("input.txt") as f:
    strings = f.read().splitlines()

nice_strings = []

for nice_candidate in strings:
    if is_nice_string(nice_candidate):
        nice_strings.append(nice_candidate)

print(len(nice_strings))
