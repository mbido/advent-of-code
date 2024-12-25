import os
import sys
sys.path.append(os.path.abspath(os.path.join(__file__, '..', '..', '..')))
import aoc_tools as aoct
from utils import *

YEAR = 2015
DAY = 3

def part_1(data):
    pos = [0, 0]
    houses = []
    for char in data:
        houses.append(str(pos[0]) + "," + str(pos[1]))
        if char == "^":
            pos[1] -= 1
        elif char == "v":
            pos[1] += 1
        elif char == "<":
            pos[0] -= 1
        else:
            pos[0] += 1    
    houses.append(str(pos[0]) + "," + str(pos[1]))
    return len(set(houses))

def part_2(data):
    santaPos = [0, 0]
    robotPos = [0, 0]
    houses = []
    for index, char in enumerate(data):
        pos = santaPos if index % 2 == 0 else robotPos
        houses.append(str(pos[0]) + "," + str(pos[1]))
        if char == "^":
            pos[1] -= 1
        elif char == "v":
            pos[1] += 1
        elif char == "<":
            pos[0] -= 1
        else:
            pos[0] += 1
        if index % 2 == 0:
            santaPos = pos
        else :
            robotPos = pos 
    pos = santaPos if len(data) % 2 == 0 else robotPos
    houses.append(str(pos[0]) + "," + str(pos[1]))
    return len(set(houses))



if __name__ == "__main__": 
    data = aoct.get_input(YEAR, DAY)
    aoct.submit_answer(YEAR, DAY, part_1(data), send=False)
    aoct.submit_answer(YEAR, DAY, part_2(data), level=2, send=False)
