def dfs(start):
    global sick
    visited[start] = 1  # 방문 했다는 것 표시해줘

    # start랑 연결되어 있는 컴퓨터들에 대해서
    for i in graph[start]:
        # 아직 방문한 적이 없다면,
        if not visited[i]:
            # dfs 재귀 호출하고, sick 누적시켜줘
            dfs(i)
            sick += 1



N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]  # idx랑 컴퓨터 번호 맞춰주기
visited = [0] * (N+1)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# print(graph) 각 번호랑 연결된 애들 넣어줬엉

sick = 0  # 바이러스 옮은 애들 몇 대인지 세어줄 변수 초기화

dfs(start=1)

print(sick)