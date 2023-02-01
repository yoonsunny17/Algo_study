from collections import deque

T = int(input())
for tc in range(1, T+1):
    l = int(input())  # 체스판 한 변의 길이
    visited = [[0]*l for _ in range(l)]
    now_x, now_y = map(int, input().split())  # 현재 나이트 좌표
    final_x, final_y = map(int, input().split())  # 타겟 나이트 좌표

    # 시계방향으로 delta
    dr = [-2, -1, 1, 2, 2, 1, -1, -2]
    dc = [1, 2, 2, 1, -1, -2, -2, -1]

    q = deque()
    q.append([now_x, now_y])
    visited[now_x][now_y] = 1

    while q:
        r, c = q.popleft()

        # 다음 지점 탐색하기 전에 지금 좌표가 타겟 좌표라면 출력 후 끝
        if r == final_x and c == final_y:
            print(visited[r][c]-1)
            break

        # 타겟 좌표가 아닌 경우에는 bfs 돌리자
        for i in range(8):
            rr = r + dr[i]
            cc = c + dc[i]

            if 0 <= rr < l and 0 <= cc < l and not visited[rr][cc]:
                visited[rr][cc] = visited[r][c] + 1
                q.append([rr, cc])