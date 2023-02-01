def dfs(start):
    # 스택 길이가 M과 동일해지면 출력 후 반환
    if len(stack) == M:
        print(' '.join(map(str, stack)))
        return
    
    # 아직 끝나지 않았으면 수열 완성해나가자
    else:
        # 중복 안되게 하려고
        for i in range(start, N+1):
            if i not in stack:
                stack.append(i)
                dfs(i+1)
                stack.pop()

N, M = map(int, input().split())
stack = []  # 수열 받을 스택
dfs(1)  # 수열 시작할 숫자 = 1