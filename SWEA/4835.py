T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    numbs = list(map(int, input().split()))
    temp = 0  # 구간 합 임시 저장해 줄 변수

    for i in range(M):
        temp += numbs[i]
    
    # 우선 최솟값, 최댓값 모두 맨 앞의 구간합으로 초기화
    minV = maxV = temp

    # 그 다음 구간합부터 비교해볼 것
    for i in range(1, N-M+1):
        temp = 0
        for j in range(i, i+M):
            temp += numbs[j]
        if maxV < temp:
            maxV = temp
        if minV > temp:
            minV = temp
    
    rlt = maxV - minV
    print(f'#{tc} {rlt}')