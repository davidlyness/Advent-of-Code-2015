# coding=utf-8
"""Advent of Code 2015, Day 10"""


def character_count(char, char_count):
    """
    Constructs string of <count of character> <character>
    :param char: character to return
    :param char_count: count of character to return
    :return: constructed string using input parameters
    """
    return str(char_count) + char


def iterate_sequence(input_string):
    """
    Calculates the next item in the Look-And-Say sequence
    :param input_string: input to the sequence iterator
    :return: next item in the sequence
    """
    output_string = ""
    current_char = None
    current_char_count = 0
    for c in input_string:
        if c == current_char:
            current_char_count += 1
        else:
            if current_char is not None:
                output_string += character_count(current_char, current_char_count)
            current_char = c
            current_char_count = 1
    output_string += character_count(current_char, current_char_count)
    return output_string


sequence = []

with open("input.txt") as f:
    sequence.append((f.read()[:-1]))

for _ in range(50):
    sequence.append(iterate_sequence(sequence[-1]))

print(len(sequence[-1]))
