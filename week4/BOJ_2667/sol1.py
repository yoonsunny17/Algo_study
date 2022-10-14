from collections import deque

N = int(input())
matrix = [list(map(int, input())) for _ in range(N)]
# visited = [[0] * N for _ in range(N)]

# delta 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# print(visited)



def bfs(a, b, graph):
    q = deque()
    q.append([a, b])
    # visited[a][b] = 1
    graph[a][b] = 0  # 방문 했으면 0으로 바꾸기
    cnt = 1

    while q:
        r, c = q.popleft()
        for i in range(4):
            rr = r + dr[i]
            cc = c + dc[i]
            # 이동하려는 지점이 범위 내에 있고, matrix에서 1인데 아직 방문 안했으면?
            # if 0 <= rr < N and 0 <= cc < N and matrix[rr][cc] == 1 and not visited[rr][cc]:
            if 0 <= rr < N and 0 <= cc < N and matrix[rr][cc] == 1:
                # 방문 기록 남겨주고, 다음 탐색 지점으로 넘겨줘
                # visited[rr][cc] = 1
                matrix[rr][cc] = 0
                q.append([rr, cc])
                cnt += 1  # 단지 수 세주기

    return cnt

danji_numbs = []  # 단지 몇 개인지 세어 줄 리스트

# start point 찾기

# 그 지점이 1인 경우에 bfs 돌리기
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1:
            danji_numbs.append(bfs(i, j, matrix))

danji_numbs.sort()  # 오름차순으로 정리해주기
print(len(danji_numbs))
for i in danji_numbs:
    print(i)
