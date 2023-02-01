# DP 점화식 규칙 찾아볼 것
# 이 문제에서는 n이 3보다 큰 경우 f(n) = f(n-1) + f(n-2) + f(n-3) 만족
def sumcase(num):
    if num == 1:
        return 1
    
    if num == 2:
        return 2

    if num == 3:
        return 4

    else:
        return sumcase(num-1) + sumcase(num-2) + sumcase(num-3)

T = int(input())
for _ in range(T):
    n = int(input())
    print(sumcase(n))
