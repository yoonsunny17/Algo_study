T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    chargers = [0] * (N+1)  # idx = 정류장 번호
    # 충전기 있는 곳을 1로 표시해주기
    for a in arr:
        chargers[a] = 1
    
    # 현재 위치, 몇 번 충전했는지 세어줄 변수
    temp, cnt = 0, 0
    d = K
    while True:
        # 만약에 최대 K만큼 갔는데 거기 충전기 있는 경우
        if chargers[temp+d] == 1:
            cnt += 1
            temp += d
            d = K
        
        # 충전기가 거기 없는 경우면 한칸씩 뒤로 가줘
        else:
            d -= 1
        
        # 만약에 d가 0이 되면 실패!
        if d == 0:
            cnt = 0
            break
        
        # 종점 도착할 때까지 방전되지 않은 경우
        if temp >= N-K:
            break
    
    print(f'#{tc} {cnt}')

    # def charging():
    #     # 현재 위치, 몇 번 충전했는지 세어줄 변수
    #     temp, cnt = 0, 0
    #     d = K
    #     while True:
    #         # 만약에 최대 K만큼 갔는데 거기 충전기 있는 경우
    #         if chargers[temp+d] == 1:
    #             cnt += 1
    #             temp += d
    #             d = K
            
    #         # 충전기가 거기 없는 경우면 한칸씩 뒤로 가줘
    #         else:
    #             d -= 1
            
    #         # 만약에 d가 0이 되면 실패!
    #         if d == 0:
    #             return 0
            
    #         # 종점 도착할 때까지 방전되지 않은 경우
    #         if temp >= N-K:
    #             return cnt


    # print(f'#{tc} {charging()}')
