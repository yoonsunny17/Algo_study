'''
투포인터 구간 합
i=0, j=1
interval_sum = 0
'''

import sys

N, S = map(int, sys.stdin.readline().split())
numbs = list(map(int, sys.stdin.readline().split()))

# 투포인터 초기값 설정해주기
start = 0
end = 1
# 구간 합은 수열의 처음값으로 초기화
interval_sum = numbs[0]
# 구간 길이 최솟값 받아줄 변수 초기화
min_rlt = float("inf")

# 구간합 반복은 end 인덱스가 범위를 초과할 때까지 반복한다
while True:
    # 구간 합이 목표값보다 크거나 같다면, start를 오른쪽으로 밀자
    if interval_sum >= S:
        # 최솟값 갱신 가능하다면 갱신해주자
        if end - start < min_rlt:
            min_rlt = end - start
        interval_sum -= numbs[start]
        start += 1

    # 종료조건
    elif end == N:
        break
  
    # 구간 합이 목표값보다 작다면, end를 왼쪽으로 당기자
    else:
        interval_sum += numbs[end]
        end += 1

if min_rlt == float("inf"):
    print(0)
else:
    print(min_rlt)