import os
import sys
sys.path.append(os.path.abspath(os.path.join(__file__, '..', '..', '..')))
import aoc_tools as aoct
from utils import *

YEAR = 2015
DAY = 23

data = aoct.get_input(YEAR, DAY)

res = 0

#data = as_grid(data)
for l in data.split("\n"):
    l = nums(l)

print(res)
