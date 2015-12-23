# coding=utf-8
"""Advent of Code 2015, Day 23, Part 2"""


def evaluate_instruction(instructions, pos, r):
    """
    Determines the next state of the computer given the current execution position and register state.
    :param instructions: reference set of instructions
    :param pos: current execution position
    :param r: state of the registers
    :return: <new execution position>, <new register state>
    """
    if instructions[pos]['op'] == "hlf":
        r[instructions[pos]['detail']] /= 2
        pos += 1
    elif instructions[pos]['op'] == "tpl":
        r[instructions[pos]['detail']] *= 3
        pos += 1
    elif instructions[pos]['op'] == "inc":
        r[instructions[pos]['detail']] += 1
        pos += 1
    elif instructions[pos]['op'] == "jmp":
        pos += int(instructions[pos]['detail'])
    elif instructions[pos]['op'] == "jie":
        if r[instructions[pos]['detail']] % 2 == 0:
            pos += int(instructions[pos]['offset'])
        else:
            pos += 1
    elif instructions[pos]['op'] == "jio":
        if r[instructions[pos]['detail']] == 1:
            pos += int(instructions[pos]['offset'])
        else:
            pos += 1
    return pos, r


with open("input.txt") as f:
    input_list = f.read().splitlines()

reference_instructions = []
for line in input_list:
    instruction = dict()
    parts = line.split()
    instruction['op'] = parts[0]
    if len(parts) == 3:
        instruction['detail'] = parts[1].replace(",", "")
        instruction['offset'] = parts[2]
    else:
        instruction['detail'] = parts[1]
    reference_instructions.append(instruction)

registers = {"a": 1, "b": 0}
position = 0
while position in range(len(reference_instructions)):
    position, registers = evaluate_instruction(reference_instructions, position, registers)

print(registers['b'])
