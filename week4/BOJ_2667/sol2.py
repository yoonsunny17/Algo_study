from pprint import pprint
from collections import deque

N = int(input())
matrix = [list(map(int, input())) for _ in range(N)]

# pprint(matrix)

'''
1. matrix에서 1인 위치를 찾는다
2. bfs 돌린다
3. matrix 1 -> 0으로 바꿔준다 (다녀감을 표시)
4. cnt 세준다 (한 단지 내에 집이 몇개인지)
5. 더이상 1이 없다면 각 단지들의 집 수 세어준 것을 arr에 담아준다
6. 오름차순으로 정렬하여 하나씩 출력한다
'''

# delta 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

arr = []  # 각 단지들의 집 수 넣어줄 리스트

def bfs(r, c, graph):
    graph[r][c] = 0  # 다녀감을 표시하기 위해 1을 0으로 바꿔주자
    cnt = 1  # 한 단지 내의  집 개수 세어줄 변수

    q = deque()
    q.append([r, c])

    while q:
        r, c = q.popleft()
        for i in range(4):
            rr = r + dr[i]
            cc = c + dc[i]
            # 만약 탐색 지점이 범위 내에 존재하고, 1인 경우라면
            if 0 <= rr < N and 0 <= cc < N and graph[rr][cc] == 1:
                graph[rr][cc] = 0
                q.append([rr, cc])
                cnt += 1
    
    return cnt


for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1:
            arr.append(bfs(i, j, matrix))

arr.sort()
print(len(arr))
for i in arr:
    print(i)
