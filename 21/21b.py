# coding=utf-8
"""Advent of Code 2015, Day 21, Part 2"""

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
armors = collections.defaultdict(dict)
rings = collections.defaultdict(dict)

weapons['Dagger']['cost'] = 8
weapons['Dagger']['damage'] = 4
weapons['Shortsword']['cost'] = 10
weapons['Shortsword']['damage'] = 5
weapons['Warhammer']['cost'] = 25
weapons['Warhammer']['damage'] = 6
weapons['Longsword']['cost'] = 40
weapons['Longsword']['damage'] = 7
weapons['Greataxe']['cost'] = 74
weapons['Greataxe']['damage'] = 8
armors['Leather']['cost'] = 13
armors['Leather']['armor'] = 1
armors['Chainmail']['cost'] = 31
armors['Chainmail']['armor'] = 2
armors['Splintermail']['cost'] = 53
armors['Splintermail']['armor'] = 3
armors['Bandedmail']['cost'] = 75
armors['Bandedmail']['armor'] = 4
armors['Platemail']['cost'] = 102
armors['Platemail']['armor'] = 5
rings['Damage +1']['cost'] = 25
rings['Damage +1']['damage'] = 1
rings['Damage +1']['armor'] = 0
rings['Damage +2']['cost'] = 50
rings['Damage +2']['damage'] = 2
rings['Damage +2']['armor'] = 0
rings['Damage +3']['cost'] = 100
rings['Damage +3']['damage'] = 3
rings['Damage +3']['armor'] = 0
rings['Defense +1']['cost'] = 20
rings['Defense +1']['damage'] = 0
rings['Defense +1']['armor'] = 1
rings['Defense +2']['cost'] = 40
rings['Defense +2']['damage'] = 0
rings['Defense +2']['armor'] = 2
rings['Defense +3']['cost'] = 80
rings['Defense +3']['damage'] = 0
rings['Defense +3']['armor'] = 3

weapon_combinations = [weapon for weapon in weapons]
armor_combinations = [''] + [armor for armor in armors]
ring_combinations = [tuple()] + [(ring,) for ring in rings] + list(itertools.permutations([ring for ring in rings], 2))

with open("input.txt") as f:
    input_list = f.read().splitlines()
boss_hp = int(input_list[0].split(": ")[1])
boss_damage = int(input_list[1].split(": ")[1])
boss_armor = int(input_list[2].split(": ")[1])

worst_cost = None

for current_equipment in itertools.product(weapon_combinations, armor_combinations, ring_combinations):
    current_stats = collections.defaultdict(dict)
    current_stats['player']['hp'] = 100
    current_stats['player']['damage'] = get_damage(current_equipment)
    current_stats['player']['armor'] = get_armor(current_equipment)
    current_stats['boss']['hp'] = boss_hp
    current_stats['boss']['damage'] = boss_damage
    current_stats['boss']['armor'] = boss_armor
    if game_winner(current_stats) == "boss":
        current_cost = get_cost(current_equipment)
        if worst_cost is None or current_cost > worst_cost:
            worst_cost = current_cost

print(worst_cost)
