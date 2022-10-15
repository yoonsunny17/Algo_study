from collections import deque

M, N, H = map(int, input().split())
matrix = [list(list(map(int, input().split())) for _ in range(N)) for _ in range(H)]

# delta 위 아래 왼쪽 오른쪽 앞 뒤
# x-axis: M // y-axis: N // z-axis: H
dx = [0, 0, -1, 1, 0, 0]
dy = [0, 0, 0, 0, 1, -1]
dz = [1, -1, 0, 0, 0, 0]


q = deque()

for k in range(H):
    for j in range(N):
        for i in range(M):
            if matrix[k][j][i] == 1:
                q.append([k, j, i])

def bfs():
    while q:
        z, y, x = q.popleft()
        for i in range(6):
            zz = z + dz[i]
            yy = y + dy[i]
            xx = x + dx[i]
            if 0 <= xx < M and 0 <= yy < N and 0 <= zz < H and matrix[zz][yy][xx] == 0:
                matrix[zz][yy][xx] = matrix[z][y][x] + 1
                q.append([zz, yy, xx])
    
    return matrix

bfs()
day = 0

for a in matrix:
    for b in a:
        for c in b:
            if c == 0:
                print(-1)
                exit(0)
            else:
                day = max(day, c)
                # if c > day:
                #     day = c

print(day - 1)