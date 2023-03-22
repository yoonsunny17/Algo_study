T = int(input())
for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    maxValue, minValue = max(arr), min(arr)
    rlt = maxValue - minValue

    print(f'#{tc} {rlt}')