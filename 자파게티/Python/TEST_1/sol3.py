# from itertools import combinations

# numbs = [1, 2, 3, 4, 5]

# arr = []

# first_combi = list(combinations(numbs, 3))

# for i in first_combi:
#     if sum(i) == 6:
#         arr.append(i)

# second_combi = list(combinations(numbs, 2))

# for j in second_combi:
#     if sum(j) == 6:
#         arr.append(j)

# print(arr)

import math

n, m = map(int, input().split())

rlt = math.factorial(n) // (math.factorial(n-m) * math.factorial(m))

print(rlt)