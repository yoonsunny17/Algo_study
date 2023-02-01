N, S = map(int, input().split())
numbs = list(map(int, input().split()))

start = 0
end = 1
interval_sum = numbs[0]
min_len = float('inf')  # 최솟값 구할 변수

while True:
    # 부분 합이 S 이상인 경우
    if interval_sum >= S:
        if end - start < min_len:
            min_len = end - start
        
        interval_sum -= numbs[start]
        start += 1
    
    # end pointer가 N과 동일한 경우
    elif end == N:
        break

    else:
        interval_sum += numbs[end]
        end += 1

if min_len == float('inf'):
    print(0)
else:
    print(min_len)