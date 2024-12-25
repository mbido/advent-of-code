import os
import sys
sys.path.append(os.path.abspath(os.path.join(__file__, '..', '..', '..')))
import aoc_tools as aoct
from utils import *

YEAR = 2024
DAY = 22

data = aoct.get_input(YEAR, DAY)

# data = """1
# 2
# 3
# 2024"""

secrets = nums(data)

P = 16777216 
N = 2000
def nth_secret(secret):
    for _ in range(N):
        a = secret * 64
        a ^= secret
        a %= P
        
        b = a // 32
        b ^= a
        b %= P
        
        c = b * 2048
        c ^= b
        c %= P
        secret = c
    return secret

print(sum(list(map(nth_secret, secrets))))

def next_secret(secret):
    a = secret * 64
    a ^= secret
    a %= P
    
    b = a // 32
    b ^= a
    b %= P
    
    c = b * 2048
    c ^= b
    c %= P
    return c


def dif_digits(secret):
    digits = []
    diff = [None]
    sequences = {}
    set_sequences = set()
    for _ in range(N+1):
        digits.append(secret % 10)
        if len(digits) >= 2:
            diff.append(digits[-1] - digits[-2])
        if len(diff) >= 5:
            sq = (diff[-4], diff[-3], diff[-2], diff[-1])
            if sq not in sequences:
                set_sequences.add(sq)
                sequences[sq] = digits[-1]
        secret = next_secret(secret)
    return digits, diff, sequences, set_sequences

L = []
D = []
S = []
all_S = set()
for s in secrets:
    # print(s)
    l, d, sq, stq = dif_digits(s)
    L.append(l)
    D.append(d)
    S.append(sq)
    all_S.update(stq)

def number_of_bananas(sq):
    res = 0
    for s in S:
        if sq in s:
            res += s[sq]
    return res

res = 0
for sq in all_S:
    res = max(res, number_of_bananas(sq))

print(res)

# print(len(L[0]))
# print(len(D[0]))
# print(len(S[0]))

