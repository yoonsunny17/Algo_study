import sys
import heapq

N = int(sys.stdin.readline())
q = []
for _ in range(N):
    numb = int(sys.stdin.readline())
    # numb가 0인 경우
    if numb == 0:
        # q가 비어있다면 0 출력해줘
        if len(q) == 0:
            print(0)
        # 비어있지 않다면 맨 위에 pop해서 출력해줘
        else:
            print(heapq.heappop(q))

    # numb가 0이 아닌 경우
    else:
        # q에 numb 넣어줘
        heapq.heappush(q, numb)