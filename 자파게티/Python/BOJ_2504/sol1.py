info = list(input())
stack = []
# print(info)

ans = 0  # 최종 출력할 값
cnt = 1  # 계산할 값

for i in range(len(info)):
    # 열린 괄호인 경우 스택에 집어넣자
    if info[i] == '(':
        stack.append(info[i])
        cnt *= 2

    elif info[i] == '[':
        stack.append(info[i])
        cnt *= 3

    # 닫힌 괄호인 경우 스택에서 괄호 꺼내서 짝 맞춰보자
    elif info[i] == ')':
        # 만약 스택이 비어있거나 짝이 안맞는 경우라면 0 출력하고 끝!
        if not stack or stack[-1] == '[':
            ans = 0
            break
        # 짝이 맞는 경우라면 지금까지 계산한 값 더해주기
        if info[i-1] == '(':
            ans += cnt
        stack.pop()
        cnt //= 2

    else:
        if not stack or stack[-1] == '(':
            ans = 0
            break
        if info[i-1] == '[':
            ans += cnt
        stack.pop()
        cnt //= 3

print(ans)