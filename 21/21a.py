# coding=utf-8
"""Advent of Code 2015, Day 21, Part 1"""

import collections
import itertools


def game_winner(game_stats):
    """
    Determines who the winner of the game will be.
    :param game_stats: player and boss statistics
    :return: whether the "player" or "boss" wins the game
    """
    active, opponent = "player", "boss"
    while game_stats['player']['hp'] > 0 and game_stats['boss']['hp'] > 0:
        game_stats[opponent]['hp'] -= max(game_stats[active]['damage'] - game_stats[opponent]['armor'], 1)
        active, opponent = opponent, active
    if game_stats['player']['hp'] > 0:
        return "player"
    else:
        return "boss"


def get_damage(equipment):
    """
    Calculates the damage value of a set of equipment.
    :param equipment: character's equipment
    :return: damage value of given equipment
    """
    damage_rating = weapons[equipment[0]]['damage']
    for ring in (equipment[2]):
        damage_rating += rings[ring]['damage']
    return damage_rating


def get_armor(equipment):
    """
    Calculates the armor value of a set of equipment.
    :param equipment: character's equipment
    :return: armor value of given equipment
    """
    if equipment[1]:
        armor_rating = armors[equipment[1]]['armor']
    else:
        armor_rating = 0
    for ring in equipment[2]:
        armor_rating += rings[ring]['armor']
    return armor_rating


def get_cost(equipment):
    """
    Calculates the cost of a set of equipment.
    :param equipment: character's equipment
    :return: cost of given equipment
    """
    cost = 0
    cost += weapons[equipment[0]]['cost']
    if equipment[1]:
        cost += armors[equipment[1]]['cost']
    for ring in equipment[2]:
        cost += rings[ring]['cost']
    return cost


weapons = collections.defaultdict(dict)
with open("weapons.txt") as f:
    input_list = f.read().splitlines()
for input_line in input_list:
    name, cost, damage, armor = input_line.split()
    weapons[name]['cost'], weapons[name]['damage'], weapons[name]['armor'] = [int(s) for s in (cost, damage, armor)]

armors = collections.defaultdict(dict)
with open("armors.txt") as f:
    input_list = f.read().splitlines()
for input_line in input_list:
    name, cost, damage, armor = input_line.split()
    armors[name]['cost'], armors[name]['damage'], armors[name]['armor'] = [int(s) for s in (cost, damage, armor)]

rings = collections.defaultdict(dict)
with open("rings.txt") as f:
    input_list = f.read().splitlines()
for input_line in input_list:
    name, cost, damage, armor = input_line.split()
    rings[name]['cost'], rings[name]['damage'], rings[name]['armor'] = [int(s) for s in (cost, damage, armor)]

weapon_combinations = [weapon for weapon in weapons]
armor_combinations = [''] + [armor for armor in armors]
ring_combinations = [tuple()] + [(ring,) for ring in rings] + list(itertools.permutations([ring for ring in rings], 2))

with open("boss.txt") as f:
    input_list = f.read().splitlines()
boss_hp = int(input_list[0].split(": ")[1])
boss_damage = int(input_list[1].split(": ")[1])
boss_armor = int(input_list[2].split(": ")[1])

best_cost = None

for current_equipment in itertools.product(weapon_combinations, armor_combinations, ring_combinations):
    current_stats = collections.defaultdict(dict)
    current_stats['player']['hp'] = 100
    current_stats['player']['damage'] = get_damage(current_equipment)
    current_stats['player']['armor'] = get_armor(current_equipment)
    current_stats['boss']['hp'] = boss_hp
    current_stats['boss']['damage'] = boss_damage
    current_stats['boss']['armor'] = boss_armor
    if game_winner(current_stats) == "player":
        current_cost = get_cost(current_equipment)
        if best_cost is None or current_cost < best_cost:
            best_cost = current_cost

print(best_cost)
