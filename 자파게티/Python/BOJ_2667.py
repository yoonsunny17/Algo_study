from collections import deque

N = int(input())
matrix = [list(map(int, input())) for _ in range(N)]

# 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(matrix, r, c):
    q = deque()
    q.append([r, c])
    matrix[r][c] = 0  # 탐색했다는 것 표시하기 위해 0으로 바꿔줄 것
    cnt = 1  # 한 단지 안에 집 개수 세어줄 변수. 초기에 1 세어줄 것

    while q:
        r, c = q.popleft()
        for i in range(4):
            rr = r + dr[i]
            cc = c + dc[i]
            # 만약 탐색 지점이 범위 내에 존재하고, 1이라면
            if 0 <= rr < N and 0 <= cc < N and matrix[rr][cc] == 1:
                # 단지에 포함되는 집 수 세어주고
                cnt += 1
                # 탐색 했다는 것 표시하고 다음 탐색 지점 넣어주자
                q.append([rr, cc])
                matrix[rr][cc] = 0

            
    
    return cnt


arr = [bfs(matrix, r, c) for r in range(N) for c in range(N) if matrix[r][c] == 1]
arr.sort()
print(len(arr))
for a in arr:
    print(a)