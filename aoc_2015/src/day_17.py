import os
import sys
sys.path.append(os.path.abspath(os.path.join(__file__, '..', '..', '..')))
import aoc_tools as aoct
from utils import *

YEAR = 2015
DAY = 17

data = aoct.get_input(YEAR, DAY)
# print(data)
res = 0

n = nums(data)

# n = [20, 15, 10, 5, 5]

cache = set()

def count(containers, eggnog):
    k = str(containers) + "-" + str(eggnog)
    if k in cache:
        return 0
    cache.add(k)
    if eggnog == 0:
        return 1
    res = 0
    for i, c in enumerate(containers):
        if eggnog >= c:
            containers[i] = 0
            res += count(containers, eggnog-c)
            containers[i] = c
            
    return res
# print(res)
print(count(n, 150))

def get_filled(containers):
    return containers.count(0)

min_cts = 150

def count(containers, eggnog):
    global min_cts
    k = str(containers) + "-" + str(eggnog)
    if k in cache:
        return 0
    cache.add(k)
    if eggnog == 0:
        cts = containers.count(0)
        min_cts = min(cts, min_cts)
        return int(cts == 4)
    res = 0
    for i, c in enumerate(containers):
        if eggnog >= c:
            containers[i] = 0
            res += count(containers, eggnog-c)
            containers[i] = c
            
    return res

# print(res)
cache = set()
print(count(n, 150))
print(min_cts)