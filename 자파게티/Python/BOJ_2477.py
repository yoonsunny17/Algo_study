# 제일 긴 h, w랑 아예 인접하지 않는 애들끼리 곱한 너비 빼주면 됨
N = int(input())
max_height, max_width = 0, 0
max_height_idx, max_width_idx = 0, 0

arr = []
for idx in range(6):
    info = list(map(int, input().split()))
    arr.append(info)

    # 가로길이인 경우
    if info[0] == 1 or info[0] == 2:
        if max_width < info[1]:
            max_width = info[1]
            max_width_idx = idx

    # 세로길이인 경우
    else:
        if max_height < info[1]:
            max_height = info[1]
            max_height_idx = idx

lst = [arr[max_height_idx-1], arr[(max_height_idx+1) % 6], arr[max_width_idx-1], arr[(max_width_idx+1) % 6]]

area = 1
for i in arr:
    if i not in lst:
        area *= i[1]

print((max_height * max_width - area) * N)
