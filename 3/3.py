# coding=utf-8
"""Advent of Code 2015, Day 3"""

santa_current_position = (0, 0)
santa_positions_visited = [santa_current_position]
robot_current_position = (0, 0)
robot_positions_visited = [robot_current_position]
current_mover = "santa"


def move(current_position, movement):
    """
    Calculates the new position of Santa / Robo-Santa, given their current position and movement vector.
    :param current_position: current position of entity
    :param movement: movement vector of entity
    :return: new position of entity
    """
    return tuple([current + movement for current, movement in zip(current_position, movement)])


with open("input.txt") as f:
    for char in f.read():
        if char == "<":
            position_diff = (-1, 0)
        elif char == ">":
            position_diff = (1, 0)
        elif char == "^":
            position_diff = (0, 1)
        elif char == "v":
            position_diff = (0, -1)
        else:
            raise ValueError(char)
        if current_mover == "santa":
            santa_current_position = move(santa_current_position, position_diff)
            santa_positions_visited.append(santa_current_position)
            current_mover = "robot"
        elif current_mover == "robot":
            robot_current_position = move(robot_current_position, position_diff)
            robot_positions_visited.append(robot_current_position)
            current_mover = "santa"
        else:
            raise ValueError(current_mover)

print(len(set(santa_positions_visited) | set(robot_positions_visited)))
