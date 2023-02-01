# bfs 사용하는 방법
# queue에 (a, 1)을 넣는다
# popleft로 뽑은 숫자에서 가능한 연산 진행
# case 1. 2를 곱했을 때 b보다 크다면 queue에 넣지 않는다
# case 2. 1을 수의 오른쪽에 추가했을 때 b보다 크면 queue에 넣지 않는다

from collections import deque

a, b = map(int, input().split())
rlt = -1
q = deque([(a, 1)])

while q:
    numb, cnt = q.popleft()
    if b == numb:
        rlt = cnt
        break

    if numb * 2 <= b:
        q.append((numb*2, cnt+1))
    
    if int(str(numb)+'1') <= b:
        q.append((int(str(numb)+'1'), cnt+1))

print(rlt)