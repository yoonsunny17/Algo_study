def dfs(i):
    if i == m:
        print(' '.join(map(str, stack)))
        return
    else:
        for j in range(1, n+1):
            # 스택이 비어있는 경우
            if len(stack) == 0:
                stack.append(j)
                dfs(i+1)
                stack.pop()
            # 스택이 비어있지 않은 경우 스택 가장 위의 숫자랑 비교해야지
            elif len(stack) != 0 and j >= stack[-1]:
                stack.append(j)
                dfs(i+1)
                stack.pop()

n, m = map(int, input().split())
stack = []

dfs(0)