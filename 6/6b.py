# coding=utf-8
"""Advent of Code 2015, Day 6, Part 2"""

import re


def get_rectangle(x1, x2, y1, y2):
    """
    Get the rectangle of lights present between a set of coordinates.
    :param x1: the lower-left coordinate of the rectangle
    :param x2: the lower-right coordinate of the rectangle
    :param y1: the upper-left coordinate of the rectangle
    :param y2: the upper-right coordinate of the rectangle
    :return: array of coordinates contained in the rectangle
    """
    coordinates = []
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            coordinates.append((x, y))
    return coordinates


def modify_light(grid, light_action, x, y):
    """
    Modifies the state of a light in the grid.
    :param grid: light grid to act on
    :param light_action: the action to perform
    :param x: x-coordinate of the light
    :param y: y-coordinate of the light
    """
    if light_action == "turn on":
        grid[x][y] += 1
    elif light_action == "turn off":
        grid[x][y] = max(grid[x][y] - 1, 0)
    elif light_action == "toggle":
        grid[x][y] += 2
    else:
        raise ValueError(light_action)


def measure_brightness(grid):
    """
    Measures the brightness of lights in the grid.
    :param grid: light grid to act on
    :return: sum of light brightness throughout grid
    """
    brightness = 0
    for row in grid:
        for light in row:
            brightness += light
    return brightness


with open("input.txt") as f:
    instructions = f.read().splitlines()

light_grid = [[0] * 1000 for _ in range(1000)]

for instruction_text in instructions:
    p = re.compile("(.*) (\d+),(\d+) through (\d+),(\d+)")
    match = p.match(instruction_text).groups()
    action = match[0]
    start_x = int(match[1])
    start_y = int(match[2])
    end_x = int(match[3])
    end_y = int(match[4])
    light_rectangle = get_rectangle(start_x, end_x, start_y, end_y)
    for coordinate in light_rectangle:
        light_x = coordinate[0]
        light_y = coordinate[1]
        modify_light(light_grid, action, light_x, light_y)

print(measure_brightness(light_grid))
