# coding=utf-8
"""Advent of Code 2015, Day 22, Part 2"""

import copy
import math

SPELLS = ["Magic Missile", "Drain", "Shield", "Poison", "Recharge"]
COSTS = {"Magic Missile": 53, "Drain": 73, "Shield": 113, "Poison": 173, "Recharge": 229}
INSTANT_DAMAGES = {"Magic Missile": 4, "Drain": 2, "Shield": 0, "Poison": 0, "Recharge": 0}
HEALS = {"Magic Missile": 0, "Drain": 2, "Shield": 0, "Poison": 0, "Recharge": 0}
DURATIONS = {"Shield": 6, "Poison": 6, "Recharge": 5}

m_cache = {}


def apply_effects(p_hp, p_mana, b_hp, b_damage, timers):
    """
    Applies spell effects to the game state.
    :param p_hp: player's current HP
    :param p_mana: player's current mana
    :param b_hp: boss's current HP
    :param b_damage: boss's damage value
    :param timers: state of spell timers
    :return: set of variables representing game state after effects have been applied
    """
    if timers["Shield"] > 0:
        player_armor = 7
    else:
        player_armor = 0
    if timers["Poison"] > 0:
        b_hp -= 3
    if timers["Recharge"] > 0:
        p_mana += 101
    for timer in timers:
        timers[timer] = max(0, timers[timer] - 1)
    return p_hp, b_hp, b_damage, player_armor, p_mana, timers


def run_boss_turn(p_hp, p_mana, b_hp, b_damage, mana_spent, timers):
    """
    Simulates the boss's turn.
    :param p_hp: player's current HP
    :param p_mana: player's current mana
    :param b_hp: boss's current HP
    :param b_damage: boss's damage value
    :param mana_spent: total mana spent by player so far in game
    :param timers: state of spell timers
    :return: game state following subsequent player turn
    """
    p_hp, b_hp, b_damage, player_armor, p_mana, timers = apply_effects(p_hp, p_mana, b_hp, b_damage, timers)
    if p_hp <= 0:
        return -1
    elif b_hp <= 0:
        return mana_spent
    else:
        return run_player_turn(p_hp - max(1, b_damage - player_armor), p_mana, player_armor,
                               b_hp, b_damage, mana_spent, timers)


def run_player_turn(p_hp, p_mana, p_armor, b_hp, b_damage, mana_spent, timers):
    """
    Simulates the player's turn
    :param p_hp: player's current HP
    :param p_mana: player's current mana
    :param p_armor: player's current armor
    :param b_hp: boss's current HP
    :param b_damage: boss's damage value
    :param mana_spent: total mana spent by player so far in game
    :param timers: state of spell timers
    :return: game state following subsequent player turn
    """
    m_key = (p_hp, b_hp, b_damage, p_armor, p_mana, mana_spent, tuple(timers))
    if m_key in m_cache:
        return m_cache[m_key]

    p_hp -= 1
    p_hp, b_hp, b_damage, p_armor, p_mana, timers = apply_effects(p_hp, p_mana, b_hp, b_damage, timers)

    if p_hp <= 0:
        return math.inf
    if b_hp <= 0:
        return mana_spent
    min_mana_spent = math.inf

    for spell in SPELLS:
        if p_mana >= COSTS[spell]:
            if spell in timers and timers[spell] > 0:
                continue
            new_timers = copy.deepcopy(timers)
            if spell in new_timers:
                new_timers[spell] = DURATIONS[spell]
            current_mama = run_boss_turn(p_hp + HEALS[spell], p_mana - COSTS[spell], b_hp - INSTANT_DAMAGES[spell],
                                         b_damage, mana_spent + COSTS[spell], new_timers)
            min_mana_spent = min(min_mana_spent, current_mama)
    m_cache[m_key] = min_mana_spent
    return min_mana_spent


with open("boss.txt") as f:
    input_list = f.read().splitlines()
boss_hp = int(input_list[0].split(": ")[1])
boss_damage = int(input_list[1].split(": ")[1])

print(run_player_turn(p_hp=50, p_mana=500, p_armor=0, b_hp=boss_hp, b_damage=boss_damage, mana_spent=0,
                      timers={"Shield": 0, "Poison": 0, "Recharge": 0}))
