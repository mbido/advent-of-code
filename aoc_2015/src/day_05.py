import os
import sys
sys.path.append(os.path.abspath(os.path.join(__file__, '..', '..', '..')))
import aoc_tools as aoct
from utils import *

YEAR = 2015
DAY = 5
    
def part_1(data):
    counter = 0
    for line in data.split("\n"):
        nbOfVowels = len([1 for char in line if char in "aeiou"])
        nbOfDouble = len([1 for index in range(len(line) - 1) if line[index] == line[index + 1]])
        nbOfWrongFollow = len([1 for index in range(len(line) - 1) if line[index] + line[index + 1] in ["ab", "cd", "pq", "xy"]])
        if nbOfVowels > 2 and nbOfDouble > 0 and nbOfWrongFollow == 0:
            counter += 1
    return counter

def part_2(data):
    counter = 0
    for line in data.split("\n"):
        nbOfCouple = len([1 for i in range(len(line) - 1) if line[i] + line[i + 1] in line[i + 2::]])
        nbOfSeparatedByOne = len([1 for i in range(len(line) - 2) if line[i] == line[i + 2]])
        if nbOfCouple > 0 and nbOfSeparatedByOne > 0:
            counter += 1
    return counter

if __name__ == "__main__": 
    data = aoct.get_input(YEAR, DAY)
    aoct.submit_answer(YEAR, DAY, part_1(data), send=False)
    aoct.submit_answer(YEAR, DAY, part_2(data), level=2, send=False)
