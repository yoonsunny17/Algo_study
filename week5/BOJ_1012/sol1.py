# from pprint import pprint
import sys
sys.setrecursionlimit(100000)

def dfs(r, c):
    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]

    for i in range(4):
        rr = r + dr[i]
        cc = c + dc[i]

        # 만약 탐색 지점이 범위 내에 존재하고 1이라면,
        if 0 <= rr < N and 0 <= cc < M and matrix[rr][cc]:
            # 0으로 만들어주고 재귀로 dfs 돌려
            matrix[rr][cc] -= 1
            dfs(rr, cc)



T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    matrix = [[0]*M for _ in range(N)]
    cnt = 0  # 지렁이 몇마리 필요한지 세어줄 변수 초기화
    for _ in range(K):
        x, y = map(int, input().split())
        matrix[y][x] = 1

    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 1:
                dfs(i, j)
                cnt += 1

    print(cnt)


