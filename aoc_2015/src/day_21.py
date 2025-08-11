import os
import sys

sys.path.append(os.path.abspath(os.path.join(__file__, "..", "..", "..")))
import aoc_tools as aoct
from utils import *

YEAR = 2015
DAY = 21

data = aoct.get_input(YEAR, DAY)


shop = re.sub(
    r" +",
    "|",
    """Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5
Damage+1    25     1       0
Damage+2    50     2       0
Damage+3   100     3       0
Defense+1   20     0       1
Defense+2   40     0       2
Defense+3   80     0       3""",
)

items = [
    (int(cost), int(damage), int(armor))
    for _, cost, damage, armor in [i.split("|") for i in shop.split("\n")]
]

COST = HP = 0
DAMAGE = 1
ARMOR = 2

ME = [100, 0, 0]
BOSS = [100, 8, 2]


def is_win(my_state, boss_state):
    if my_state[HP] <= 0:
        return False
    boss_state[HP] -= my_state[DAMAGE] - boss_state[ARMOR]
    if boss_state[HP] <= 0:
        return True
    my_state[HP] -= boss_state[DAMAGE] - my_state[ARMOR]
    return is_win(my_state, boss_state)


print(is_win(ME, BOSS))
