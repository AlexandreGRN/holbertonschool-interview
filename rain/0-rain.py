#!/usr/bin/python3
"""
Water retain algo
"""


def rain(walls):
    water_retain = 0
    if (len(walls) == 0):
        return 0
    for height in range(max(walls) + 1):
        water_retain_last_puddle = 0
        in_puddle = False
        for column in range(len(walls)):
            if (walls[column] >= height and in_puddle):
                in_puddle = False
                water_retain += water_retain_last_puddle
                water_retain_last_puddle = 0
            if (in_puddle):
                water_retain_last_puddle += 1
            if (walls[column] >= height):
                in_puddle = True
    return water_retain
