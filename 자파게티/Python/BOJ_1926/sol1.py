from collections import deque
from pprint import pprint

def bfs(r, c):
    q = deque()
    q.append([r, c])
    visited[r][c] = 1
    width = 1  # 그림 넓이 출력할 변수

    while q:
        r, c = q.popleft()
        for i in range(4):
            rr = r + dr[i]
            cc = c + dc[i]

            # 탐색 지점이 범위 내에 존재하는 경우
            if 0 <= rr < n and 0 <= cc < m:
                # 그 지점이 1이고 아직 방문한 적이 없다면
                if matrix[rr][cc] == 1 and not visited[rr][cc]:
                    # 방문 처리 해주고
                    visited[rr][cc] = visited[r][c] + 1
                    width += 1
                    # 다음 탐색 지점에 넣어줘
                    q.append([rr, cc])

    return width

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

# delta 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

cnt = 0  # 그림 개수 구할 변수
max_width = 0  # 그림 최대 넓이 구할 변수
for i in range(n):
    for j in range(m):
        # 행렬이 1이고 아직 방문한 적이 없는 곳이라면 bfs 돌리고, 그림 개수 세어줘
        if matrix[i][j] == 1 and not visited[i][j]:
            max_width = max(max_width, bfs(i, j))
            cnt += 1

print(cnt)
print(max_width)