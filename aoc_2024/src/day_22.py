import os
import sys
sys.path.append(os.path.abspath(os.path.join(__file__, '..', '..', '..')))
import aoc_tools as aoct
from utils import *

YEAR = 2024
DAY = 22

data = aoct.get_input(YEAR, DAY)
# print(data)

data = """1
2
3
2024"""

secrets = nums(data)

P = 16777216
N = 2000
def next_secret(secret):
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

# print(sum(list(map(next_secret, secrets))))


def next_secret(secret):
    digits = []
    diffs = [-20]
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
        digits.append(secret % 10)
        if len(digits) > 1:
            diffs.append(digits[-1] - digits[-2])
    return digits, diffs

digits = []
diffs = []
max_digit = []
max_digit_sequences = []
sequences = set()
for s in secrets:
    d, df = next_secret(s)
    digits.append(d)
    diffs.append(df)
    
    for i in range(4, len(df)):
        sq = (df[i-3], df[i - 2], df[i - 1], df[i])
        sequences.add(sq)
    # diffs.add(tuple(df))
    
    max_digit.append(max(d))
    # print(max_digit[-1])
    # break
I = 0
def first_sequence(sequence):
    # global I
    # print(I)
    # I += 1
    
    res = 0
    for i in range(len(digits)):
        dig = digits[i]
        dif = diffs[i]
        for j in range(3, len(dig)):
            if (dif[j - 3], dif[j - 2], dif[j - 1], dif[j]) == sequence:
                res += dig[j]
                # print(dig[j])
                break
    return res

# N = 8
# size = len(sequences) // N
# i = 7

sequences = list(sequences)
# print(first_sequence((-2,1,-1,3)))

res = 0

l = len(sequences)
for i in range(l):
    # print(f"{i} -> {res}")
    sq = random.choice(sequences)
    sequences.remove(sq)
    r = first_sequence(sq)
    if r > res:
        res = r
        print(f"{i} -> {res}")


print(f"result : {res}")
# ss = sorted(sequences, key=first_sequence)
# print(max(list(map(first_sequence, sequences))))
# res = 0

# #data = as_grid(data)
# for l in data.split("\n"):
#     l = nums(l)

# print(res)