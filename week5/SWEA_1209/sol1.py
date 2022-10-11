T = 10
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(100)]

    max_row, max_col, max_d1, max_d2 = 0, 0, 0, 0

    arr = []  # 최댓값 담을 리스트 초기화
    
    # max_row
    for i in range(len(matrix)):
        row_sum = 0
        for j in range(len(matrix)):
            row_sum += matrix[i][j]
            if row_sum > max_row:
                max_row = row_sum
    
    # max_col
    for j in range(len(matrix)):
        col_sum = 0
        for i in range(len(matrix)):
            col_sum += matrix[i][j]
            if col_sum > max_col:
                max_col = col_sum
    
    # max_d1
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            d1_sum = 0
            if i == j:
                d1_sum += matrix[i][j]

    # max_d2
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            d2_sum = 0
            if i + j == 99:
                d2_sum += matrix[i][j]
    

    arr.append([max_col, max_row, d1_sum, d2_sum])

    print(f'#{tc} {max(arr[0])}')