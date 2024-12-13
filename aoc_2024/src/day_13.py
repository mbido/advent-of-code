import os
import sys
sys.path.append(os.path.abspath(os.path.join(__file__, '..', '..', '..')))
import aoc_tools as aoct
from utils import *

YEAR = 2024
DAY = 13

def part_1(data):
    res = 0
    dx = dy = 0
    for c in data.split("\n\n"):
        xa, ya, xb, yb, xp, yp = nums(c)
        
        # a * xa + b * xb = xp 
        # a * ya + b * yb = yp
        
        # a = (xp - b * xb) / xa
        # (xp - b * xb) / xa * ya + b * yb = yp
        
        # a = (xp - b * xb) / xa
        # (xp - b * xb) * ya + b * yb * xa = yp * xa
        
        # a = (xp - b * xb) / xa
        # xp - b * xb + b * yb * xa / ya = yp * xa / ya
        
        # a = (xp - b * xb) / xa
        # - b * xb + b * yb * xa / ya = yp * xa / ya - xp
        
        # a = (xp - b * xb) / xa
        # b * (yb * xa / ya - xb)  = yp * xa / ya - xp
        
        
        b = ((yp + dy) * xa / ya - (xp + dx)) / (yb * xa / ya - xb)
        a = ((xp + dx) - b * xb) / xa
        
        if abs(round(b) - b) < 0.001 and abs(round(a) - a) < 0.001:
            a = round(a)
            b = round(b)
            res += 3 * a + b
    return res

def part_2(data):
    res = 0
    dx = dy = 0
    for c in data.split("\n\n"):
        xa, ya, xb, yb, xp, yp = nums(c)
        
        xp += 10_000_000_000_000
        yp += 10_000_000_000_000
        
        b = ((yp + dy) * xa / ya - (xp + dx)) / (yb * xa / ya - xb)
        a = ((xp + dx) - b * xb) / xa
        
        if abs(round(b) - b) < 0.001 and abs(round(a) - a) < 0.001:
            a = round(a)
            b = round(b)
            res += 3 * a + b
    return res


if __name__ == "__main__": 
    data = aoct.get_input(YEAR, DAY)
    aoct.submit_answer(YEAR, DAY, part_1(data), send=False)
    aoct.submit_answer(YEAR, DAY, part_2(data), level=2, send=False)
