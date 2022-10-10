T = 10
for tc in range(1, T+1):
    N = int(input())  # 덤프 횟수
    boxes = list(map(int, input().split()))  # 상자 높이 담긴 리스트

    for i in range(N):
        max_box = max(boxes)
        min_box = min(boxes)
        max_idx = boxes.index(max_box)
        min_idx = boxes.index(min_box)

        boxes[max_idx] -= 1
        boxes[min_idx] += 1

    print(f'#{tc} {max(boxes)-min(boxes)}')