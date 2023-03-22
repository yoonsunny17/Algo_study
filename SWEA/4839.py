def search(pages, target):
    left, right = 1, pages
    cnt = 0

    while True:
        middle = (left + right) // 2

        if target == middle:
            return cnt
        
    #     # 찾는 쪽수가 중간 페이지보다 더 큰 값인 경우
    #     # left을 middle값으로 갱신해줘
        if target > middle:
            left = middle
            cnt += 1

    #     # 찾는 쪽수가 중간 페이지보다 더 작은 값인 경우
    #     # right를 middle값으로 갱신해줘
        elif target < middle:
            right = middle
            cnt += 1

T = int(input())
for tc in range(1, T+1):
    P, A, B = map(int, input().split())

    a = search(P, A)
    b = search(P, B)
    
    if a < b:
        rlt = 'A'
    elif a > b:
        rlt = 'B'
    else:
        rlt = 0

    print(f'#{tc} {rlt}')