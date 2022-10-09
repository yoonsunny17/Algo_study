T = 10
for tc in range(1, T+1):
    N = int(input())
    buildings = list(map(int, input().split()))
    cnt = 0

    # 좌 우 0, 0 빼고 생각하기
    for i in range(2, len(buildings)-2):
        # i번째 건물이 양 옆 2개씩 빌딩보다 높은 경우라면, 양 옆 건물들 중 최고 높이 뭔지 구해줘
        if buildings[i] > buildings[i-1] and buildings[i] > buildings[i-2] and buildings[i] > buildings[i+1] and buildings[i] > buildings[i+2]:
            rlt = max(buildings[i-1], buildings[i-2], buildings[i+1], buildings[i+2])
            # 그 다음에 조망권 획득한 세대 수 cnt로 세어주자
            cnt += buildings[i] - rlt

    print(f'#{tc} {cnt}')
