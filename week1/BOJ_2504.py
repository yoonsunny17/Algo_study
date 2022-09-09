# (, ), [, ]
# () = 2, [] = 3, (x) = 2 x value, [x] = 3 x value
# 여는 괄호들은 stack에 넣어주고, 닫는 괄호 나오면 꺼내서 계산해주자

strings = list(input())
stack = []
ans = 0  # 최종 결과값
cnt = 1  # 현재 값, 계속 갱신해줄 변수!

for i in range(len(strings)):
    if strings[i] == "(":
        stack.append(strings[i])
        cnt *= 2
    
    elif strings[i] == "[":
        stack.append(strings[i])
        cnt *= 3
    
    # 닫힌 소괄호가 나타났다!
    elif strings[i] == ")":
        # 근데 stack이 비어있거나, 마지막이 열린 중괄호라면 짝이 안맞네
        if not stack or stack[-1] == "[":
            ans = 0
            break
        # 만약에 그 직전이 열린 소괄호라면 최종 결과값 갱신해주기
        if strings[i-1] == "(":
            ans += cnt
        stack.pop()
        cnt //= 2
    
    # 닫힌 중괄호가 나타났다!
    else:
        # 근데 stack이 비어있거나, 마지막이 열린 소괄호라면 짝이 안맞아
        if not stack or stack[-1] == "(":
            ans = 0
            break
        # 만약에 그 직전이 열린 중괄호라면 최종 결과값 갱신해주기
        if strings[i-1] == "[":
            ans += cnt
        stack.pop()
        cnt //= 3

# 짝이 제대로 맞춰지지 않는다면 0 출력, 잘 맞으면 최종 결과값 출력해줘
if stack:
    print(0)
else:
    print(f'{ans}')