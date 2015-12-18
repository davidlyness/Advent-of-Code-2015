# coding=utf-8
"""Advent of Code 2015, Day 18, Part 2"""


def get_light_state(grid, row, column):
    """
    Determines the current state of a light in the grid.
    :param grid: reference grid of lights
    :param row: row number of light to check
    :param column: column number of light to check
    :return: 1 if light is on, 0 otherwise
    """
    if row in range(len(grid)) and column in range(len(grid)):
        return grid[row][column]
    else:
        return 0


def get_next_light_state(grid, row, column):
    """
    Determines what the next state of a light should be, based on its neighbours and position
    :param grid: reference grid of lights
    :param row: row number of light
    :param column: column number of light
    :return: 1 if light should be on, 0 otherwise
    """
    if row in (0, len(grid) - 1) and column in (0, len(grid) - 1):
        return 1
    else:
        num_on_neighbours = 0
        num_on_neighbours += get_light_state(grid, row - 1, column - 1)
        num_on_neighbours += get_light_state(grid, row - 1, column)
        num_on_neighbours += get_light_state(grid, row - 1, column + 1)
        num_on_neighbours += get_light_state(grid, row, column - 1)
        num_on_neighbours += get_light_state(grid, row, column + 1)
        num_on_neighbours += get_light_state(grid, row + 1, column - 1)
        num_on_neighbours += get_light_state(grid, row + 1, column)
        num_on_neighbours += get_light_state(grid, row + 1, column + 1)
        if grid[row][column] == 1:
            if num_on_neighbours in (2, 3):
                return 1
            else:
                return 0
        else:
            if num_on_neighbours == 3:
                return 1
            else:
                return 0


def iterate_lights(grid):
    """
    Calculates the next grid in the light sequence
    :param grid: reference grid of lights
    :return: next grid in sequence
    """
    next_grid = [[0 for _ in range(len(grid))] for _ in range(len(grid))]
    for row_num in range(len(grid)):
        for column_num in range(len(grid[row_num])):
            next_grid[row_num][column_num] = get_next_light_state(grid, row_num, column_num)
    return next_grid


def count_lights(grid):
    """
    Count the number of lights turned on in the grid.
    :param grid: light grid to act on
    :return: number of lights turned on in the grid
    """
    num_lights_on = 0
    for line in grid:
        for light in line:
            if light == 1:
                num_lights_on += 1
    return num_lights_on


grid_size = 100
lights = [[0 for _ in range(grid_size)] for _ in range(grid_size)]

row = 0
with open("input.txt") as f:
    input_list = f.read().splitlines()
for input_line in input_list:
    column = 0
    for c in input_line:
        if c == "#":
            state = 1
        else:
            state = 0
        lights[row][column] = state
        column += 1
    row += 1

num_iterations = 100
for _ in range(num_iterations):
    lights = iterate_lights(lights)

print(count_lights(lights))
