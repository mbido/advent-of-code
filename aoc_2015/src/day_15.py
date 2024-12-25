import os
import sys
sys.path.append(os.path.abspath(os.path.join(__file__, '..', '..', '..')))
import aoc_tools as aoct
from utils import *

YEAR = 2015
DAY = 15

data = aoct.get_input(YEAR, DAY)
# print(data)
res = 0

# data = """Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
# Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3"""


cache = {}
def best_score(ing, ts, qtt, part):
    if ts == 0:
        c = d = f = t = ca = 0
        for i, ig in enumerate(ing):
            c += ig[0] * qtt[i]
            d += ig[1] * qtt[i]
            f += ig[2] * qtt[i]
            t += ig[3] * qtt[i]
            ca += ig[4] * qtt[i]
            
        c = max(0, c)
        d = max(0, d)
        f = max(0, f)
        t = max(0, t)
        # print(f"{qtt} -> {c * d * f * t}")
        if part == 2 and ca != 500:
            return 0
        return max(0, c * d * f * t)

    k = tuple(qtt + [ts])
    if k in cache:
        return cache[k]
    
    scores = []
    for i, ig in enumerate(ing):
        qtt[i] += 1
        scores.append(best_score(ing, ts - 1, qtt, part))
        qtt[i] -= 1
        
    cache[k] = max(scores)
    return max(scores)


#data = as_grid(data)
ing = []
for l in data.split("\n"):
    ing.append(s_nums(l))

print(best_score(ing, 100, [0 for _ in ing], 1))
cache = {}
print(best_score(ing, 100, [0 for _ in ing], 2))