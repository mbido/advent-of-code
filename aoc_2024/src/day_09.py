import os
import sys
sys.path.append(os.path.abspath(os.path.join(__file__, '..', '..', '..')))
import aoc_tools as aoct
from utils import *

YEAR = 2024
DAY = 9

def add_first(tab):
    end = -1
    for i, e in enumerate(tab[::-1]):
        if e != -1:
            end = e
            tab[len(tab) - 1 - i] = -1
            break
    if end == -1:
        return False
        
    for i, e in enumerate(tab):
        if e == -1:
            tab[i] = end
            return True
    return False

def is_sorted(tab):
    index = -1
    for i, e in enumerate(tab):
        if e == -1:
            index = i
            break
    for i in range(index, len(tab)):
        if tab[i] != -1:
            return False
    return True

def part_1(data):
    # data ="2333133121414131402"
    d = [int(e) for e in data]
    tab = []
    for i in range(len(d) // 2):
        a = d[i * 2]
        b = d[i * 2 + 1]
        for _ in range(a):
            tab.append(i)
        for _ in range(b):
            tab.append(-1)
    if (len(d) % 2 == 1):
        a = d[-1]
        for _ in range(a):
            tab.append(len(d) // 2)
    
    while not is_sorted(tab):
        add_first(tab)
    # print(tab)
    
    res = 0
    for i, e in enumerate(tab):
        if e == -1:
            break
        res += i * e
    return res

def move2(map, void, e):
    i1, size1 = map[e]
    for j, v in enumerate(void):
        i2, size2 = v
        if i2 > i1:
            return
        if size1 <= size2:
            map[e][0] = i2
            void[j][1] = size2 - size1
            void[j][0] = i2 + size1
            return

def part_2(data):
    map = []
    void = []
    index = 0
    for i, e in enumerate(data):
        e = int(e)
        if i % 2 == 1:
            if e > 0:
                void.append([index, e])
            index += e
        else:
            map.append([index, e])
            index += e
    for i in range(len(map) - 1, -1, -1):
        move2(map, void, i)
    
    res = 0
    for i, e in enumerate(map):
        j, size = e
        res += int(i * size * (j + (size - 1) / 2))
    return res

if __name__ == "__main__": 
    data = aoct.get_input(YEAR, DAY)
    aoct.submit_answer(YEAR, DAY, part_1(data), send=False)
    aoct.submit_answer(YEAR, DAY, part_2(data), level=2, send=False)
