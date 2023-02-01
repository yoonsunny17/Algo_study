# deque.rotate() 메서드 --> n만큼 왼쪽(-n) 또는 오른쪽(+n)으로 리스트 이동시킬 수 있음
import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
q = deque([x for x in range(1, n+1)])
removed = []

while q:
    # q 내부를 왼쪽으로 k-1만큼 이동시켜서 k번째 요소가 맨 왼쪽에 오도록 하자
    q.rotate(-(k-1))
    removed.append(q.popleft())

print(f'<{", ".join(map(str, removed))}>')