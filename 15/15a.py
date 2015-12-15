# coding=utf-8
"""Advent of Code 2015, Day 15, Part 1"""

import re


def get_score(ing, amounts):
    """
    Calculates the score of a specific recipe, given ingredient properties and amounts.
    :param ing: matrix of ingredient property values
    :param amounts: number of teaspoons of each ingredient to include
    :return: total recipe score
    """
    score = 1
    for i in range(len(ing[0]) - 1):
        score *= max(sum([amounts[j] * ing[j][i] for j in range(len(amounts))]), 0)
    return score


with open("input.txt") as f:
    input_list = f.read().splitlines()

ingredients = []
best_score = 0

for line in input_list:
    p = re.compile("(.*): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)")
    match = p.match(line).groups()
    ingredients.append([int(match[1]), int(match[2]), int(match[3]), int(match[4]), int(match[5])])

for ing_one_amount in range(100):
    for ing_two_amount in range(100 - ing_one_amount):
        for ing_three_amount in range(100 - ing_one_amount - ing_two_amount):
            ing_four_amount = 100 - ing_one_amount - ing_two_amount - ing_three_amount
            current_score = get_score(ingredients, [ing_one_amount, ing_two_amount, ing_three_amount, ing_four_amount])
            if current_score > best_score:
                best_score = current_score

print(best_score)
