import os
import sys
sys.path.append(os.path.abspath(os.path.join(__file__, '..', '..', '..')))
import aoc_tools as aoct
from utils import *

YEAR = 2015
DAY = 12

def part_1(data):
    numbers = [int(elt) for elt in re.findall("-?[0-9]+", data)]
    return sum(numbers)

def sum_numbers(json_data):
    if isinstance(json_data, int):
        return json_data
    if isinstance(json_data, list):
        return sum(sum_numbers(elt) for elt in json_data)
    if isinstance(json_data, dict):
        if "red" in json_data.values():
            return 0
        return sum(sum_numbers(elt) for elt in json_data.values())
    return 0

def part_2(data):
    json_data = json.loads(data)
    return sum_numbers(json_data)

if __name__ == "__main__": 
    data = aoct.get_input(YEAR, DAY)
    aoct.submit_answer(YEAR, DAY, part_1(data), send=False)
    aoct.submit_answer(YEAR, DAY, part_2(data), level=2, send=False)
