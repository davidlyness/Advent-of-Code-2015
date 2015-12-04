# coding=utf-8
"""Advent of Code 2015, Day 4"""

import hashlib

hash_found = False
answer_candidate = 0

with open("input.txt") as f:
    secret = f.read()

while not hash_found:
    hashed_string = hashlib.md5((secret + str(answer_candidate)).encode()).hexdigest()
    if hashed_string[:6] == "000000":
        print(answer_candidate)
        hash_found = True
    answer_candidate += 1
