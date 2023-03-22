T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbs = list(map(int, input()))

    count = [0] * 10  # 0 ~ 9 까지 카운트 해줄 리스트

    for numb in numbs:
        count[numb] += 1
    
    # 가장 많은 카드 개수
    max_card = 0
    for i in range(len(count)):
        if count[i] >= max_card:
            max_card = count[i]
            max_numb = i
    
    print(f'#{tc} {max_numb} {max_card}')
