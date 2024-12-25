import os
import sys
sys.path.append(os.path.abspath(os.path.join(__file__, '..', '..', '..')))
import aoc_tools as aoct
from utils import *

YEAR = 2024
DAY = 24

data = aoct.get_input(YEAR, DAY)

s1, s2 = data.split("\n\n")

S = z3.Solver()

variables = {}
for r in s1.split("\n"):
    n, v = r.split(": ")
    v = v == '1'
    variables[n] = z3.Bool(n)
    S.add(variables[n] == v)
    
# print(S)

for r in s2.split("\n"):
    v1, opp, v2, _, v3 = r.split(" ")
    if v1 not in variables:
        variables[v1] = z3.Bool(v1)
    if v2 not in variables:
        variables[v2] = z3.Bool(v2)
    if v3 not in variables:
        variables[v3] = z3.Bool(v3)
    if opp == "AND":
        o = z3.And(variables[v1], variables[v2])
    elif opp == "XOR":
        o = z3.Xor(variables[v1], variables[v2])
    elif opp == "OR":
        o = z3.Or(variables[v1], variables[v2])
    else:
        o = "ERROR"
        print(opp)
    S.add(variables[v3] == o)

if S.check() == z3.unsat:
    print("ERROR")

model = S.model()
res = sorted([(n, z3.is_true(model[variables[n]])) for n in variables if n[0] == "z"], key=lambda e: e[0], reverse=True)
# print(res)
res = [str(int(e[1])) for e in res]
print(int("0b" + "".join(res), 2))


# part2
S = z3.Solver()
variables = {}

vs = set(re.findall(r'([0-9a-z]{3})', data))
swapped = []
for v in vs:
    variables[v] = z3.Bool(v)
    variables[v + '_'] = z3.Int(v + '_')
    swapped.append(variables[v + '_'])
    S.add(z3.Or(variables[v + '_'] == 0, variables[v + '_'] == 1))

S.add(z3.Sum(swapped) == 8)

X = 0
Y = 0
for r in s1.split("\n"):
    n, v = r.split(": ")
    v = v == '1'
    # variables[n] = z3.Bool(n)
    S.add(variables[n] == v)
    
    if n[0] == 'x':
        X <<= 1
        X += int(v)
    else :
        Y <<= 1
        Y += int(v)
Z = X + Y
zb = bin(Z)[2:]

for i, b in enumerate(zb[::-1]):
    n = "z" + str(i // 10) + str(i % 10)
    variables[n] = z3.Bool(n)
    S.add(variables[n] == (b == '1'))



for i, r in enumerate(s2.split("\n")):
    v1, opp, v2, _, v3 = r.split(" ")

    if opp == "AND":
        res = z3.And(variables[v1], variables[v2])
    elif opp == "XOR":
        res = z3.Xor(variables[v1], variables[v2])
    elif opp == "OR":
        res = z3.Or(variables[v1], variables[v2])
    else:
        res = "ERROR"
        print(opp)
        
    p1 = z3.And(variables[v3 + '_'] == 0, variables[v3] == res) # no swap for v3
    bloc = []
    for v in variables.keys():
        # print(f"{len(variables.keys())}, {len(v)}")
        if len(v) != 3 or v == v3:
            continue
        # print(v)
        bloc.append(z3.And(variables[v + '_'] == 1, variables[v] == res))
    # print(f"{len(variables)} - {len(bloc)}")
    if not bloc:
        print("bloc is empty")
        exit(1)
        
    # p2 = z3.And(variables[v3 + '_'] == 1, z3.AtLeast(*bloc, 1), z3.AtMost(*bloc, 1)) # exactly one swap for v3
    p2 = z3.And(variables[v3 + '_'] == 1, z3.Or(bloc))
    S.push()
    S.add(z3.Or(p1, p2))
    # print(f"line {i} over {len(s2.split("\n"))} : {r} <= ") 
    # c = S.check()
    # print(c) 
    # if c == z3.unsat:
    #     S.pop()
    #     print("UNSAT!")
    #     print(r)
    #     # print(p1)
    #     # print(p2)
    #     # exit(1)


if S.check() == z3.unsat:
    print("ERROR : Solver is unsat")
    exit(1)

model = S.model()
print(",".join(sorted([n[:-1] for n in variables.keys() if n[-1] == '_' and model[variables[n]] == 1])))