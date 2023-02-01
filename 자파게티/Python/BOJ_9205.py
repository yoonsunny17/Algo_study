from collections import deque

def bfs():
    q = deque()
    q.append([home_x, home_y])

    while q:
        x, y = q.popleft()
        if abs(fes_x-x) + abs(fes_y-y) <= 1000:
            print('happy')
            return
        for i in range(n):  # 편의점들 방문해보자
            if not visited[i]:  # 아직 방문한 적 없는 편의점이라면
                xx, yy = arr[i]
                # 범위 내의 거리에 편의점 있으면
                if abs(x-xx) + abs(y-yy) <= 1000:
                    # 방문표시 해주고 다음 탐색지점에 담아주자
                    visited[i] = 1
                    q.append([xx, yy])
    print('sad')
    return


t = int(input())
for _ in range(t):
    n = int(input())
    home_x, home_y = map(int, input().split())
    arr = []
    for _ in range(n):
        x, y = map(int, input().split())
        arr.append([x, y])
    fes_x, fes_y = map(int, input().split())
    visited = [0 for _ in range(n+1)]
    bfs()

