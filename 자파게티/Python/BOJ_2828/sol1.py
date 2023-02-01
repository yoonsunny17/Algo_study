'''
다시 한번 생각해보고 풀어보기
'''
n, m = map(int, input().split())
j = int(input())

# 바구니 왼쪽 오른쪽 끝
start, end = 1, m
distance = 0

for _ in range(j):
    apple = int(input())

    # 사과 위치가 바구니 안에 위치해 있는 경우
    if apple >= start and apple <= end:
        continue

    # 사과 위치가 바구니 왼쪽 끝보다 더 왼쪽에 위치해 있는 경우
    if apple < start:
        distance += start - apple
        start = apple
        end = apple + m - 1

    # 사과 위치가 바구니 오른쪽 끝보다 더 오른쪽에 위치해 있는 경우
    elif apple > end:
        distance += apple - end
        start = apple - m + 1
        end = apple
    
print(distance)