import os
import sys
sys.path.append(os.path.abspath(os.path.join(__file__, '..', '..', '..')))
import aoc_tools as aoct
from utils import *

YEAR = 2015
DAY = 13

def get_score(nameList, heatMap):
    res = 0
    res += heatMap[nameList[0]][nameList[-1]] + heatMap[nameList[-1]][nameList[0]]
    for i in range(len(nameList) - 1):
        res += heatMap[nameList[i]][nameList[i + 1]] + heatMap[nameList[i + 1]][nameList[i]]
    return res

def part_1(data):
    heatMap = {}
    nameSet = set()
    for line in data.split("\n"):
        factor = 1 if "gain" in line else -1
        p1, nb, p2 = re.match(r"(\w+) .* (\d+) .* (\w+).", line).groups()
        if not p1 in heatMap:
            heatMap[p1] = {}
        heatMap[p1][p2] = factor * int(nb)
        nameSet.add(p1)
        nameSet.add(p2)
    nameList = list(nameSet)
    res = float('-inf')
    for p in permutations(nameList):
        res = max(res, get_score(p, heatMap))
    return res

def part_2(data):
    heatMap = {}
    nameSet = set()
    for line in data.split("\n"):
        factor = 1 if "gain" in line else -1
        p1, nb, p2 = re.match(r"(\w+) .* (\d+) .* (\w+).", line).groups()
        if not p1 in heatMap:
            heatMap[p1] = {}
        heatMap[p1][p2] = factor * int(nb)
        nameSet.add(p1)
        nameSet.add(p2)
    nameList = list(nameSet)
    heatMap["_MOI_"] = {cle : 0 for cle in nameList}
    nameList.append("_MOI_")
    for person in heatMap:
        heatMap[person]["_MOI_"] = 0
    res = float('-inf')
    for p in permutations(nameList):
        res = max(res, get_score(p, heatMap))
    return res

if __name__ == "__main__": 
    data = aoct.get_input(YEAR, DAY)
    aoct.submit_answer(YEAR, DAY, part_1(data), send=False)
    aoct.submit_answer(YEAR, DAY, part_2(data), level=2, send=False)
