'''
왜 틀리는건가...?
'''
from pprint import pprint
from collections import deque

# 1 = 익은 토마토, 0 = 익지 않은 토마토, -1 = 토마토 없음
# matrix[z][y][x] 인덱스 순서 주의!
M, N, H = map(int, input().split())
matrix = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
# visited = [[[0]*M for _ in range(N)] for _ in range(H)]

# delta
# 위, 아래, 왼쪽, 오른쪽, 앞, 뒤
dx = [0, 0, -1, 1, 0, 0]  # M
dy = [0, 0, 0, 0, 1, -1]  # N
dz = [1, -1, 0, 0, 0, 0]  # H
# pprint(matrix)

# for i in range(N):
#     for j in range(M):
#         for k in range(H):
#             if matrix[k][j][i] == 1:
#                 print(k, j, i)

def bfs(x, y, z):
    # visited[z][y][x] = 1 # 익은 토마토 확인!
    q = deque()
    q.append([x, y, z])
    # cnt = 0
    
    while q:
        x, y, z = q.popleft()
        for i in range(6):
            xx = x + dx[i]
            yy = y + dy[i]
            zz = z + dz[i]
            # 탐색 지점이 범위 내에 존재하고, 0이고, 아직 방문한 적이 없다면
            if 0 <= xx < M and 0 <= yy < N and 0 <= zz < H and not matrix[zz][yy][xx]:
                # 방문 표시 해주고, 0 -> 1 바꿔주고, 다음 탐색 지점으로 넘겨주기
                # visited[zz][yy][xx] = 1
                matrix[zz][yy][xx] = matrix[z][y][x] + 1
                q.append([xx, yy, zz])
                # cnt += 1

    return matrix

for k in range(H):
    for j in range(N):
        for i in range(M):
            if matrix[k][j][i] == 1:
                bfs(i, j, k)
                # print(i, j, k)
                # print(f'{i} {j} {k}')

# pprint(matrix)

# 다 익었다면 matrix의 최댓값 - 1 출력,
# 원래 다 익어있었다면 0
# matrix에 0이 하나라도 남아있으면 -1 출력

day = 0  # 최댓값 담아줄 변수 초기화
# for k in range(H):
#     for j in range(N):
#         for i in range(M):
#             if matrix[k][j][i] == 0:
#                 print(-1)
#                 exit(0)
#             else:
#                 day = max(day, matrix[k][j][i])

for k in matrix:
    for j in k:
        for i in j:
            if i == 0:
                print(-1)
                exit(0)
            else:
                day = max(day, i)

print(day-1)
