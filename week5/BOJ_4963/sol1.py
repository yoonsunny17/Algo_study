from pprint import pprint
import sys
sys.setrecursionlimit(100000)

def dfs(r, c):
    matrix[r][c] = 0
    # delta 상 하 좌 우 ,, 우상 우하 좌하 좌상
    dr = [0, 0, -1, 1, 1, 1, -1, -1]
    dc = [-1, 1, 0, 0, -1, 1, 1, -1]

    for i in range(8):
        rr = r + dr[i]
        cc = c + dc[i]
        # 탐색 지점이 범위 내에 존재하고, 1인 경우라면
        if 0 <= rr < h and 0 <= cc < w and matrix[rr][cc] == 1:
            matrix[rr][cc] = 0
            dfs(rr, cc)

while True:
    w, h = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(h)]

    cnt = 0  # 섬의 개수 세는 변수 초기화
    for i in range(h):
        for j in range(w):
            if matrix[i][j] == 1:
                dfs(i, j)
                cnt += 1
    
    # 종료 조건
    if w == 0 and h == 0:
        break

    print(cnt)