from pprint import pprint

n, m = map(int, input().split())
arr = [list(x for x in range(n)) for _ in range(m)]

pprint(arr)

for i in range(n):
    for j in range(m):
        print(arr[i][j + (m-1 + 2*j) * (i%2)])

# pprint(arr)