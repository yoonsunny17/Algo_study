N, S = map(int, input().split())
numbs = list(map(int, input().split()))

arr = []  # 부분합 만족하는 수열 길이 담을 배열
interval_sum = 0
end = 0

for start in range(N):
    # 부분합이 S 보다 작고 end pointer가 N보다 작은 동안
    while interval_sum < S and end < N:
        # 계속 합해주고
        interval_sum += numbs[end]
        # end pointer 오른쪽으로 이동
        end += 1

    # 만약에 부분합이 S 이상이면
    if interval_sum >= S:
        # 부분합 수열 길이를 arr에 넣어주자
        arr.append(end-start+1)

    # 그다음에 start pointer 옮겨줄건데 그 전에 값 빼주기
    interval_sum -= numbs[start]

if len(arr) == 0:
    print(0)
else:
    print(min(arr))