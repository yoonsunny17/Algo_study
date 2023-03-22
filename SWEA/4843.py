from collections import deque

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbs = list(map(int, input().split()))
    numbs.sort()
    q = deque(numbs)

    arr = []

    for i in range(10):
        if i % 2 == 0:
            arr.append(q.pop())
        else:
            arr.append(q.popleft())

    print(f'#{tc}', end=' ')
    print(*arr)