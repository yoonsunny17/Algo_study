from collections import deque

n, k = map(int, input().split())
max_numb = 100000
time = [0] * (max_numb + 1)

q = deque()
q.append(n)  # 언니 위치 넣어주기

while q:
    # q에서 언니가 움직일 위치 하나 꺼내와
    x = q.popleft()
    # 언니가 걷거나 순간이동 시 움직일 수 있는 위치 배열
    lst = [x-1, x+1, 2*x]
    
    # 언니랑 동생이랑 만나게 된다면 출력 끝
    if x == k:
        print(time[x])
        break

    # 움직이는 경우 세 가지 고려해보자
    for dx in lst:
        # 움직일 위치가 범위 내에 있고, 아직 방문한 적이 없다면
        if 0 <= dx <= max_numb and not time[dx]:
            # 시간 누적해주고 다음 탐색지점으로 넣어줘
            time[dx] = time[x] + 1
            q.append(dx)