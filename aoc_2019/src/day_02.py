import os
import sys
sys.path.append(os.path.abspath(os.path.join(__file__, '..', '..', '..')))
import aoc_tools as aoct
from utils import *

YEAR = 2019
DAY = 2

def compute(in1, in2, data):
    data[1] = in1
    data[2] = in2
    for i in range(0, len(data)-4, 4):
        a, b, c, d = data[i:i+4]
        if a == 99:
            break
        temp = data[b] + data[c] if a == 1 else data[b] * data[c]
        data[d] = temp
    return data[0]

def part_1(data):
    d = [int(e) for e in data.split(",")]
    return compute(12, 2, d)

def part_2(data):
    for noun in range(100):
        for verb in range(100):
            d = [int(e) for e in data.split(",")]
            if compute(noun, verb, d) == 19690720:
                return 100 * noun + verb
    return "ERROR"

if __name__ == "__main__": 
    data = aoct.get_input(YEAR, DAY)
    aoct.submit_answer(YEAR, DAY, part_1(data), send=False)
    aoct.submit_answer(YEAR, DAY, part_2(data), level=2, send=False)
