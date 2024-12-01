import os
import sys
sys.path.append(os.path.abspath(os.path.join(__file__, '..', '..', '..')))
import aoc_tools as aoct
from utils import *

YEAR = 2024
DAY = 1

def part_1(data):
    L, R = [], []
    for line in data.split("\n"):
        l, r = line.split("   ")
        L.append(int(l))
        R.append(int(r))
    
    L.sort()
    R.sort()
    
    res = 0
    for i in range(len(L)):
        res += max(L[i], R[i]) - min(L[i], R[i])
    
    return res

def part_2(data):
    L, R = [], []
    for line in data.split("\n"):
        l, r = line.split("   ")
        L.append(int(l))
        R.append(int(r))
    res = 0
    for elt in L:
        res += elt * R.count(elt)
    
    return res

if __name__ == "__main__": 
    data = aoct.get_input(YEAR, DAY)
    aoct.submit_answer(YEAR, DAY, part_1(data), send=False)
    aoct.submit_answer(YEAR, DAY, part_2(data), level=2, send=False)
