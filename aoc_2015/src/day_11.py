import os
import sys
sys.path.append(os.path.abspath(os.path.join(__file__, '..', '..', '..')))
import aoc_tools as aoct
from utils import *

YEAR = 2015
DAY = 11

def increments_string(string):
    string = list(string)
    for i in range(len(string) - 1, -1, -1):
        letter = string[i] 
        if letter != "z":
            string[i] = chr(ord(letter) + 1)
            return ''.join(string)
        string[i] = "a"
    return ''.join(string)

def check_pass(string):
    check = False
    for i in range(len(string) - 2):
        if string[i] == chr(ord(string[i + 1]) - 1) == chr(ord(string[i + 2]) - 2):
            check = True
            break
    if not check:
        return False
    if re.search(r'[iol]', string) != None:
        return False
    if re.search(r'(.)\1.*([^\1])\2', string) == None:
        return False
    return True

def part_1(data):
    password = increments_string(data)
    while not check_pass(password):
        password = increments_string(password)
    return password

def part_2(data):
    password = increments_string(part_1(data))
    while not check_pass(password):
        password = increments_string(password)
    return password

if __name__ == "__main__": 
    data = aoct.get_input(YEAR, DAY)
    aoct.submit_answer(YEAR, DAY, part_1(data), send=False)
    aoct.submit_answer(YEAR, DAY, part_2(data), level=2, send=False)
