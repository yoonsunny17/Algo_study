import sys

N, M, V = map(int, sys.stdin.readline().split())
graph = [[0]*(N+1) for _ in range(N+1)]
visited = [0] * (N+1)

# 간선이 연결하는 두 정점 번호 연결시키기
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    # 해당 노드들이 연결되어있으면 행렬의 요소값 1로 바꿔주기
    graph[a][b] = graph[b][a] = 1

# 깊이 우선 탐색 (dfs)
def dfs(V):
    # 방문했으면 출력하고 끝
    visited[V] = 1
    print(V, end='')

    # 방문한 적이 없고 그래프에서 연결되어 있는 곳이라면 재귀 돌려줘!
    for i in range(1, N+1):
        if visited[i] == 0 and graph[V][i] == 1:
            dfs(i)


# 너비 우선 탐색 (bfs)
def bfs(V):
    # 큐 생성해서 방문할 곳 넣어주기
    queue = [V]

    # dfs 먼저 돌렸으니까 visited가 1로 되어있을 테니까 반대로 체크해줄 것
    visited[V] = 0

    while queue:
        V = queue.pop(0)
        print(V, end=' ')

        for i in range(1, N+1):
            if visited[i] == 1 and graph[V][i] == 1:
                queue.append(i)
                visited[i] = 0

dfs(V)
print()
bfs(V)
