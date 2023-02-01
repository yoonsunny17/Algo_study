import sys, heapq

N = int(sys.stdin.readline())
q = []
for _ in range(N):
    numb = int(sys.stdin.readline())
    # numb가 0인 경우
    if numb == 0:
        # q가 비어있으면 0 출력
        if len(q) == 0:
            print(0)
        # 아니면 가장 큰 수 출력해줘
        else:
            print(-1 * heapq.heappop(q))

    # numb가 0이 아닌 경우
    else:
        # q에 숫자 넣어줘
        heapq.heappush(q, -numb)