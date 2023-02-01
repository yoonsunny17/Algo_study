def dfs(i, N, M):
    # i = stack의 index값 ; M과 동일해지면 출력
    if i == M:
        print(' '.join(map(str, stack)))
    
    # stack이 아직 다 차지 않았으면 수열 계속 만들자
    else:
        for j in range(1, N+1):
            # 중복되지 않도록, stack에 있다면 추가하지 말자
            if j not in stack:
                stack.append(j)
                dfs(i+1, N, M)
                stack.pop()  # 여기가 백트래킹 핵심!

N, M = map(int, input().split())
stack = []  # 수열 받을 스택

dfs(0, N, M)