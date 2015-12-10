# coding=utf-8
"""Advent of Code 2015, Day 7, Part 2"""

with open("input.txt") as f:
    instructions = f.read().splitlines()

operations = dict()

for instruction in instructions:
    (left_inst, right_inst) = instruction.split(" -> ")
    operations[right_inst] = left_inst.split(" ")


def compute_wire(wire, known_wires):
    """
    Recursively computes the value for a particular wire.
    :param wire: the current wire to calculate the value for
    :param known_wires: the set of wires whose values are already known
    :return: the specified wire's value
    """
    try:
        return int(wire)
    except ValueError:
        pass

    if wire not in known_wires:
        wire_operator = operations[wire]
        if len(wire_operator) == 1:
            wire_value = compute_wire(wire_operator[0], known_wires)
        else:
            operator_name = wire_operator[-2]
            if operator_name == "AND":
                wire_value = compute_wire(wire_operator[0], known_wires) & compute_wire(wire_operator[2], known_wires)
            elif operator_name == "LSHIFT":
                wire_value = compute_wire(wire_operator[0], known_wires) << compute_wire(wire_operator[2], known_wires)
            elif operator_name == "NOT":
                wire_value = ~compute_wire(wire_operator[1], known_wires)
            elif operator_name == "OR":
                wire_value = compute_wire(wire_operator[0], known_wires) | compute_wire(wire_operator[2], known_wires)
            elif operator_name == "RSHIFT":
                wire_value = compute_wire(wire_operator[0], known_wires) >> compute_wire(wire_operator[2], known_wires)
            else:
                wire_value = None
        known_wires[wire] = wire_value
    return known_wires[wire]


# Override wire b and reset all signals
operations['b'] = [compute_wire("a", dict())]

print(compute_wire("a", dict()))
