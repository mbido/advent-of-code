import os
import sys

sys.path.append(os.path.abspath(os.path.join(__file__, "..", "..", "..")))
import aoc_tools as aoct
from utils import *

YEAR = 2015
DAY = 20

data = aoct.get_input(YEAR, DAY)

data = int(data)


def get_number_gifts1(n_house):
    divs = get_divisors(n_house)
    return sum(divs) * 10


def part1():
    i = 1
    while True:
        if get_number_gifts1(i) >= data:
            return i
        i += 1


def get_number_gifts2(n_house):
    divs = get_divisors(n_house)
    res = 0
    for d in divs:
        if d * 50 < n_house:
            continue
        res += 11 * d
    return res


def part2():
    i = 1
    while True:
        if get_number_gifts2(i) >= data:
            return i
        i += 1


print(part1())
print(part2())
