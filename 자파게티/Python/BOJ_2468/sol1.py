'''
미완성 코드
'''

from collections import deque
from pprint import pprint

def bfs(board):
    q = deque()



N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
board = [[1] * N for _ in range(N)]

numbs = [0] * 101  # matrix 안에 존재하는 높이 체크해주기
for i in range(N):
    for j in range(N):
        if numbs[matrix[i][j]] == 0:
            numbs[matrix[i][j]] = 1

cnt = 0  # 안전 영역 몇개인지 세어 줄 변수

# 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for i in range(len(numbs)):
    if numbs[i] == 1:
        height = i
        for r in range(N):
            for c in range(N):
                if matrix[r][c] <= height:
                    board[r][c] = 0

        # pprint(board)
        bfs(board)