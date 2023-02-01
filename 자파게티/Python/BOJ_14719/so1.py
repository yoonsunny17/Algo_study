H, W = map(int, input().split())
heights = list(map(int, input().split()))

ans = 0  # 물 얼마나 고였는지 출력할 변수

# 특정 기둥의 양 옆 기둥들이 더 높아야지 물이 고인다!
# 맨 끝 기둥들은 각자 범위 조심해주기
for i in range(1, W-1):
    left_height = max(heights[:i])
    right_height = max(heights[i+1:])

    # 둘 중 더 낮은 기둥만큼 물이 최대로 고이겠지
    shorter = min(left_height, right_height)

    if heights[i] < shorter:
        ans += shorter - heights[i]

print(ans)

