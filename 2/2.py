# coding=utf-8
"""Advent of Code 2015, Day 2"""


def present_surface_area(dimensions):
    """
    Calculates the surface area of a present.
    :param dimensions: array of [length, width, height] of a present
    :return: surface area of present
    """
    l, w, h = dimensions
    return (2 * l * w) + (2 * w * h) + (2 * h * l)


def present_slack(dimensions):
    """
    Calculates the amount of slack required per present.
    :param dimensions: array of [length, width, height] of a present:
    :return: amount of slack for present
    """
    l, w, h = dimensions
    return min(l * w, w * h, h * l)


def present_ribbon(dimensions):
    """
    Calculates the amount of ribbon required for present.
    :param dimensions: array of [length, width, height] of a present:
    :return: amount of ribbon for present
    """
    l, w, h = dimensions
    return min(2 * (l + w), 2 * (w + h), 2 * (h + l))


def present_volume(dimensions):
    """
    Calculates the volume of a present.
    :param dimensions: array of [length, width, height] of a present
    :return: volume of present
    """
    l, w, h = dimensions
    return l * w * h


total_paper = 0
total_ribbon = 0

with open("input.txt") as f:
    dimension_text = f.read().splitlines()

for present_string in dimension_text:
    present_dimensions = [int(x) for x in present_string.split("x")]
    total_paper += present_surface_area(present_dimensions) + present_slack(present_dimensions)
    total_ribbon += present_ribbon(present_dimensions) + present_volume(present_dimensions)

print("Total paper: " + str(total_paper))
print("Total ribbon: " + str(total_ribbon))
