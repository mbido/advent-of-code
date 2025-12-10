import os
import sys

sys.path.append(os.path.abspath(os.path.join(__file__, "..", "..", "..")))
import aoc_tools as aoct
from utils import *

YEAR = 2025
DAY = 10

data = aoct.get_input(YEAR, DAY)

res = 0

# graphs
# node_patern = r'[a-z]{2}'
# V = list(set(re.findall(node_patern, data)))
# V_T = {V[i] : i for i in range(len(V))}
# # Not directed
# edges = [(V_T[a], V_T[b]) for a, b in re.findall(r'(node_patern)\-(node_patern)', data)]
# G = ig.Graph(edges=edges, directed=False)
# # Directed
# edges = [(V_T[a], V_T[b], int(c)) for a, b, c in re.findall(r'(node_patern)\-(node_patern)\-(\d+)', data)]
# G = ig.Graph(edges=[(s,t) for s,t,_ in edges], directed=False, edge_attrs={"weight": [w for _,_,w in edges]})

# data = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
# [...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
# [.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"""


def parsing(set_string):
    res = eval(set_string)
    if type(res) == int:
        return [res]
    return list(res)


def taking(sets_taken, template_machine):
    real_machine = [0] * len(template_machine)
    for s in sets_taken:
        for i in s:
            real_machine[i] = (real_machine[i] + 1) % 2
    return all(
        [template_machine[i] == real_machine[i] for i in range(len(template_machine))]
    )


# data = as_grid(data)
for l in data.split("\n"):
    machine = eval(l.split(" ")[0].replace(".", "0,").replace("#", "1,"))
    sets = [parsing(elt) for elt in re.findall(r"\([\d,]+\)", l)]
    # print(machine, sets)

    found = False
    for n in range(1, len(sets) + 1):
        if found:
            break
        for s in combinations(sets, n):
            if taking(s, machine):
                res += n
                found = True
                break

print(res)


def solver(sets: List[List[int]], machine: List[int]):
    N = len(machine)
    K = len(sets)

    model = pulp.LpProblem()
    x = pulp.LpVariable.dicts("take", range(K), lowBound=0, cat="Integer")

    model += pulp.lpSum(x[j] for j in range(K))  # to minimize

    for i in range(N):  # with constrains
        Ax = []  # matrix vector product
        for j in range(K):
            A_ij = 1 if i in sets[j] else 0
            Ax.append(A_ij * x[j])
        model += pulp.lpSum(Ax) == machine[i]

    # model.solve()
    model.solve(pulp.PULP_CBC_CMD(msg=False))

    return int(pulp.value(model.objective))


res = 0
for l in data.split("\n"):
    machine = eval(l.split(" ")[-1].replace("{", "[").replace("}", "]"))
    sets = [parsing(elt) for elt in re.findall(r"\([\d,]+\)", l)]
    # print(machine, sets)
    res += solver(sets, machine)

print(res)
