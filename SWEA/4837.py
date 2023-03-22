from itertools import combinations

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [x for x in range(1, 13)]
    cnt = 0
    for combi in combinations(arr, N):
        if sum(combi) == K:
            cnt += 1

    print(f'#{tc} {cnt}')
