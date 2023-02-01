# (A, F) (B, D) (C, E)
# (0, 5) (1, 3) (2, 4)
N = int(input())
dice = []  # 전체 주사위 정보 담아 줄 배열 선언
for _ in range(N):
    dice.append(list(map(int, input().split())))

# 윗면 아랫면 마주보는 애들
pair_numbs = {
    0: 5,
    1: 3,
    2: 4,
    3: 1,
    4: 2,
    5: 0,
}

# key가 아랫면(또는 윗면)인 경우, 옆면이 되는 values
sides = {
    0: [1, 2, 3, 4],
    1: [0, 2, 4, 5],
    2: [0, 1, 3, 5],
    3: [0, 2, 4, 5],
    4: [0, 1, 3, 5],
    5: [1, 2, 3, 4],
}

# 최종 값 출력해 줄 변수 선언
answer = 0

# 첫 번째 주사위의 윗면을 생각해보자 (어짜피 아랫면은 필요없엉)
for i in range(6):
    top_idx = pair_numbs[i]
    top_numb = dice[0][top_idx]
    side_idx = sides[i]

    # 옆면이 가능한 숫자들 중 최댓값을 temp에 저장해줘
    temp = max(dice[0][idx] for idx in side_idx)

    # 두번째 주사위부터는 아랫면, 윗면 둘 다 고려해줘
    # 아랫면 숫자 고려하는 것 외에는 첫번째 주사위랑 동일한 과정으로!
    for j in range(1, len(dice)):
        bottom_idx = dice[j].index(top_numb)
        top_idx = pair_numbs[bottom_idx]
        top_numb = dice[j][top_idx]
        side_idx = sides[bottom_idx]

        temp += max(dice[j][idx] for idx in side_idx)

    # answer와 temp 값 비교하면서 최댓값 갱신
    if answer < temp:
        answer = temp

print(answer)
