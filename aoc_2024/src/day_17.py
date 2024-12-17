import os
import sys
sys.path.append(os.path.abspath(os.path.join(__file__, '..', '..', '..')))
import aoc_tools as aoct
from utils import *

YEAR = 2024
DAY = 17

combo = [0, 1, 2, 3, "A", "B", "C"]

def get_combo(op, reg):
    return op if op < 4 else reg[ord(combo[op]) - ord("A")]

def adv(op, reg):
    reg[0] = int(reg[0] / 2**get_combo(op, reg))

def bxl(op, reg):
    reg[1] = reg[1] ^ op

def bst(op, reg):
    reg[1] = get_combo(op, reg) % 8
    
def jnz(op, reg):
    return -1 if reg[0] == 0 else op

def bxc(_, reg):
    reg[1] = reg[1] ^ reg[2]

def out(op, reg):
    return get_combo(op, reg) % 8

def bdv(op, reg):
    reg[1] = int(reg[0] / 2**get_combo(op, reg))

def cdv(op, reg):
    reg[2] = int(reg[0] / 2**get_combo(op, reg))

def run(prog, reg):
    inst = [adv, bxl, bst, jnz, bxc, out, bdv, cdv]
    res = []
    index = 0
    while index < len(prog) - 1:
        f = inst[prog[index]]
        op = prog[index + 1]
        if f == out:
            o = out(op, reg)
            res.append(o)
            index += 2
        elif f == jnz:
            i = jnz(op, reg)
            index = index + 2 if i == -1 else i
        else:
            f(op, reg)
            index += 2
    return res

def part_1(data):
    s1, s2 = data.split("\n\n")
    reg = nums(s1)
    prog = nums(s2)
    res = [str(e) for e in run(prog, reg)]
    return ",".join(res)

def valid(A):
    am1 = (A & 7) ^ 1
    v1 = ((am1 ^ (A >> am1) ^ 4) & 7) == 2
    a3m1 = (int(A / 3) & 7) ^ 1
    v2 = ((a3m1 ^ (int(A / 3) >> a3m1) ^ 4) & 7) == 4
    return v1 and v2

def find(A, expected, prog):
    res = set()
    for a in A:
        a <<= 3
        for i in range(8):
            reg = [a + i, 0, 0]
            o = run(prog, reg)
            if o == expected:
                res.add(a + i)
    return res

def part_2(data):
    _, s2 = data.split("\n\n")
    prog = nums(s2)
    A_list = set()
    A_list.add(0)
    for i in range(len(prog) - 1, -1, -1):
        A_list = find(A_list, prog[i:], prog)
    return min(A_list)

if __name__ == "__main__": 
    data = aoct.get_input(YEAR, DAY)
    aoct.submit_answer(YEAR, DAY, part_1(data), send=False)
    aoct.submit_answer(YEAR, DAY, part_2(data), level=2, send=False)
