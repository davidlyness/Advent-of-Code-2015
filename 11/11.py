# coding=utf-8
"""Advent of Code 2015, Day 11"""

import re


def has_triple_straight(string):
    """
    Determines whether a string has a triple straight (e.g. of the form "abc") contained within it.
    :param string: candidate to check
    :return: whether a triple straight is present
    """
    for i in range(len(string) - 2):
        candidate = string[i:i + 3]
        first_letter = candidate[0]
        if candidate == first_letter + chr(ord(first_letter) + 1) + chr(ord(first_letter) + 2):
            return True
    return False


def has_forbidden_characters(string):
    """
    Determines whether a string has any forbidden characters contained within it.
    :param string: candidate to check
    :return: whether the forbidden characters are present
    """
    return any(char in string for char in ["i", "o", "l"])


def has_multiple_double_letters(string):
    """
    Determines whether a string has multiple double letters (e.g. of the form "aa" and "ss") contained within it
    :param string: candidate to check
    :return: whether multiple double letters are present
    """
    return len(re.findall(r'([a-z])\1', string)) >= 2


def is_valid_password(string):
    """
    Determines whether a string is a valid password.
    :param string: candidate to check
    :return: whether the string is a valid password
    """
    return not has_forbidden_characters(string) and has_triple_straight(string) and has_multiple_double_letters(string)


def get_next_password_candidate(string):
    """
    Calculates what the next password candidate should be.
    :param string: current password candidate
    :return: next password candidate
    """
    return re.sub(r"([a-y])(z*)$", lambda x: chr(ord(x.group(1)) + 1) + len(x.group(2)) * "a", string)


def get_next_valid_password(string):
    """
    Calculates the next valid password in sequence.
    :param string: the current password
    :return: the next valid password
    """
    while not is_valid_password(string):
        string = get_next_password_candidate(string)
    return string


with open("input.txt") as f:
    password = f.read()[:-1]

password = get_next_valid_password(password)
print("Part 1: " + password)

password = get_next_valid_password(get_next_password_candidate(password))
print("Part 2: " + password)
