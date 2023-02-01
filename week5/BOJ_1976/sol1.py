import sys
sys.setrecursionlimit(100000)

from pprint import pprint

def union(x, y):
    a = find(x)
    b = find(y)

    parent[max(a, b)] = min(a, b)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

N = int(input())
M = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
plan = map(int, input().split())

parent = [x for x in range(N)]

for i in range(N):
    for j in range(N):
        # 서로 연결되어있는데 부모가 같지 않으면
        if matrix[i][j] == 1 and find(i) != find(j):
            # 유니온 연산 고고
            union(i, j)

# 집합 rlt 만들어주고, 여행계획에 포함된 M개의 나라에 대해 조상을 각각 찾아주자
rlt = set()
for i in range(M):
    rlt.add(parent[i])

if len(rlt) == 1:
    print('YES')
else:
    print('NO')
