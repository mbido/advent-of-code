import os
import sys
sys.path.append(os.path.abspath(os.path.join(__file__, '..', '..', '..')))
import aoc_tools as aoct
from utils import *

YEAR = 2016
DAY = 1

def part_1(data):
    dir = 0 # ["north", "east", "south", "ouest"]
    pos = [0, 0]
    for instruction in data.split(", "):
        a = instruction[0]
        b = int(instruction[1:])
        
        if a == "L":
            dir += 3
            dir = dir % 4
        else :
            dir += 1
            dir = dir % 4
        
        i = 0 if dir % 2 == 0 else 1
        sign = 1 if 0 < dir < 3 else -1
        
        pos[i] += sign * b
        
    return abs(pos[0]) + abs(pos[1])

def part_2(data):
    dir = 0 # ["north", "east", "south", "ouest"]
    pos = [0, 0]
    map = []
    map.append(str(pos))
    for instruction in data.split(", "):
        a = instruction[0]
        b = int(instruction[1:])
        
        if a == "L":
            dir += 3
            dir = dir % 4
        else :
            dir += 1
            dir = dir % 4
        
        i = 0 if dir % 2 == 0 else 1
        sign = 1 if 0 < dir < 3 else -1
        
        for _ in range(b):
            pos[i] += sign
            if str(pos) in map:
                return abs(pos[0]) + abs(pos[1])
            map.append(str(pos))
    return "ERROR"

if __name__ == "__main__": 
    data = aoct.get_input(YEAR, DAY)
    aoct.submit_answer(YEAR, DAY, part_1(data), send=False)
    aoct.submit_answer(YEAR, DAY, part_2(data), level=2, send=False)
