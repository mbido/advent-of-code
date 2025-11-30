import os
import sys

sys.path.append(os.path.abspath(os.path.join(__file__, "..", "..", "..")))
import aoc_tools as aoct
from utils import *

YEAR = 2015
DAY = 21

data = aoct.get_input(YEAR, DAY)


weapons = re.sub(
    r" +",
    "|",
    """Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0""",
)

weapons = [
    (int(cost), int(damage), int(armor))
    for _, cost, damage, armor in [i.split("|") for i in weapons.split("\n")]
]

armors = re.sub(
    r" +",
    "|",
    """Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5""",
)

armors = [
    (int(cost), int(damage), int(armor))
    for _, cost, damage, armor in [i.split("|") for i in armors.split("\n")]
]
armors.append((0, 0, 0))

rings = re.sub(
    r" +",
    "|",
    """Damage+1    25     1       0
Damage+2    50     2       0
Damage+3   100     3       0
Defense+1   20     0       1
Defense+2   40     0       2
Defense+3   80     0       3""",
)


rings = [
    (int(cost), int(damage), int(armor))
    for _, cost, damage, armor in [i.split("|") for i in rings.split("\n")]
]
rings.append((0, 0, 0))
rings.append((0, 0, 0))


# print(weapons)
# print(armors)
# print(rings)

# indexes
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


def can_win(gold, my_state, boss_state):
    # take one weapon
    for w in weapons:
        # take at most one armor:
        for a in armors:
            # take one or two rings
            for idx, r1 in enumerate(rings):
                for r2 in rings[:idx] + rings[idx + 1 :]:
                    if gold < w[COST] + a[COST] + r1[COST] + r2[COST]:
                        continue
                    state = [
                        my_state[HP],
                        my_state[DAMAGE] + w[DAMAGE] + r1[DAMAGE] + r2[DAMAGE],
                        my_state[ARMOR] + a[ARMOR] + r1[ARMOR] + r2[ARMOR],
                    ]
                    # print(state)
                    if is_win(copy.copy(state), copy.copy(boss_state)):
                        # print(state, w, a, r1, r2)
                        return True
    return False


g = 0
while True:
    g += 1
    if can_win(g, copy.copy(ME), copy.copy(BOSS)):
        print(g)
        break


def can_lose(gold, my_state, boss_state):
    # take one weapon
    for w in weapons:
        # take at most one armor:
        for a in armors:
            # take one or two rings
            for idx, r1 in enumerate(rings):
                for r2 in rings[:idx] + rings[idx + 1 :]:
                    if gold < w[COST] + a[COST] + r1[COST] + r2[COST]:
                        continue
                    state = [
                        my_state[HP],
                        my_state[DAMAGE] + w[DAMAGE] + r1[DAMAGE] + r2[DAMAGE],
                        my_state[ARMOR] + a[ARMOR] + r1[ARMOR] + r2[ARMOR],
                    ]
                    # print(state)
                    if not is_win(copy.copy(state), copy.copy(boss_state)):
                        # print(state, w, a, r1, r2)
                        return True
    return False


for g in range(1000000, 0, -1):
    if can_lose(g, copy.copy(ME), copy.copy(BOSS)):
        print(g)
        break
