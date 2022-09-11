H, W = map(int, input().split())
pillars = list(map(int, input().split()))

ans = 0

# 내 좌, 우에 더 높은 높이의 기둥이 있다면 물이 고여
for i in range(1, W-1):
    left_pillar = max(pillars[:i])
    right_pillar = max(pillars[i+1:])

    # 그 중에서 더 짧은 기둥이 뭔지를 알아야해
    # 그게 물이 고이는 것의 기준점이 될 것
    short_pillar = min(left_pillar, right_pillar)

    if pillars[i] < short_pillar:
        ans += short_pillar - pillars[i]
    
print(f'{ans}')