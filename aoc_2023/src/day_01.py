import os
import sys
sys.path.append(os.path.abspath(os.path.join(__file__, '..', '..', '..')))
import aoc_tools as aoct
from utils import *

YEAR = 2023
DAY = 1

def part_1(data):
    res = 0
    for line in data.split("\n"):
        a = b = 0
        for l in line:
            if "0" <= l <="9" :
                a = int(l)
                break
        for l in line[::-1]:
            if "0" <= l <="9" :
                b = int(l)
                break
        res += a * 10 + b
    return res

def spelled(num: str, backward: bool = False):
    l = len(num)
    if backward:
        a = num[-3:]
        b = num[-4:]
        c = num[-5:]
    else:
        a = num[:3]
        b = num[:4]
        c = num[:5]
        
    if l >= 3:
        match a:
            case "one":
                return 1
            case "two":
                return 2
            case "six":
                return 6
    if l >= 4:
        match b:
            case "four":
                return 4
            case "five":
                return 5
            case "nine":
                return 9
    if l >= 5:
        match c:
            case "three":
                return 3
            case "seven":
                return 7
            case "eight":
                return 8
    return 0 # == False

def part_2(data):
    res = 0
    for line in data.split("\n"):
        a = b = 0
        for i in range (len(line)):
            l = line[i]
            if "0" <= l <="9" :
                a = int(l)
                break
            t = spelled(line[i:])
            if t:
                a = t
                break
            
        for i in range (len(line) - 1, -1, -1):
            l = line[i]
            if "0" <= l <= "9" :
                b = int(l)
                break
            
            t = spelled(line[:i + 1], True)
            print(line[:i + 1], t)
            if t:
                b = t
                break
        print(a, b)
        res += a * 10 + b
    return res

if __name__ == "__main__":
    data = aoct.get_input(YEAR, DAY)
    aoct.submit_answer(YEAR, DAY, part_1(data), send=False)
    aoct.submit_answer(YEAR, DAY, part_2(data), level=2, send=False)
