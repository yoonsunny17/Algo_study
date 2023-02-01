import sys

N = int(sys.stdin.readline())
numbs = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
check = list(map(int, sys.stdin.readline().split()))
for i in check:
    print(1) if i in numbs else print(0)