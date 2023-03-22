T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 10 * 10 격자 이차원 리스트
    matrix = [[0] * 10 for _ in range(10)]

    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())

        # color 가 1이면 matrix에 1로 채우고, 2면 2를 채워서 결과가 3인 영역 카운트해서 출력하면 되겠다
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                # 같은 영역도 겹치게 주어지는 경우라면 이렇게 풀어야 할듯
                if matrix[i][j] == 0 and color == 1:
                    matrix[i][j] += 1
                if matrix[i][j] == 0 and color == 2:
                    matrix[i][j] += 2
                if matrix[i][j] == 1 and color == 2:
                    matrix[i][j] += 2
                if matrix[i][j] == 2 and color == 1:
                    matrix[i][j] += 1

                # 영역이 겹치게 주어지지 않는다고 할 때
                # if color == 1:
                #     matrix[i][j] += 1
                # if color == 2:
                #     matrix[i][j] += 2
        
        cnt = 0
        for i in range(10):
            for j in range(10):
                if matrix[i][j] == 3:
                    cnt += 1
        
    print(f'#{tc} {cnt}')