S = list(map(str, input()))
T = list(map(str, input()))

# t에서 s로
# 1. 뒤에 A 제거
# 2. 뒤에 B 제거 후 문자열 뒤집기

while True:
    if len(T) == len(S):
        break

    if T[-1] == 'A':
        T.pop()
    
    elif T[-1] == 'B':
        T.pop()
        T = T[::-1]

print(1) if S == T else print(0)