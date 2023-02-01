'''
테케는 맞으나 틀렸다고 나옴..
'''

from collections import deque

def bfs(board):
    visited = [[0] * n for _ in range(n)]
    cnt = 0  # 안전영역 개수 세어줄 변수
    for r in range(n):
        for c in range(n):
            # 영역이 1이고 아직 방문한 적이 없으면
            # bfs 돌리고 안전영역 개수 세어주기
            if board[r][c] == 1 and not visited[r][c]:
                q = deque()
                q.append([r, c])
                visited[r][c] = 1

                while q:
                    r, c = q.popleft()
                    for i in range(4):
                        rr = r + dr[i]
                        cc = c + dc[i]
                        # 탐색 지점이 범위 내에 존재하고 보드 값이 1이면서 아직 방문한 적이 없다면
                        if 0 <= rr < n and 0 <= cc < n and board[rr][cc] == 1 and not visited[rr][cc]:
                            visited[rr][cc] = visited[r][c] + 1
                            q.append([rr, cc])

                cnt += 1

    return cnt

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
board = [[1] * n for _ in range(n)]

# delta 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

numbs = [0] * 101  # 높이는 1이상 100이하
# 높이가 될 수 있는 애들 체크해주기
for i in range(n):
    for j in range(n):
        if numbs[matrix[i][j]] == 0:
            numbs[matrix[i][j]] = 1

max_rlt = 0  # 최대 안전 영역 출력할 변수 설정

for i in range(len(numbs)):
    if numbs[i] == 1:
        height = i

        for r in range(n):
            for c in range(n):
                if matrix[r][c] <= height:
                    board[r][c] = 0

        max_rlt = max(max_rlt, bfs(board))

print(max_rlt) if max_rlt != 0 else print(1)
