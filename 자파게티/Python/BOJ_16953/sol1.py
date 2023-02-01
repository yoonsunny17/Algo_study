A, B = map(int, input().split())
cnt = 1

while True:
    # B == A: break
    if B == A:
        break
    # B가 홀수인데 1의 자리수가 1이 아닌 경우, B가 A보다 작은 경우 끝!
    elif (B % 2 != 0 and B % 10 != 1) or (B < A):
        cnt = -1
        break
    
    # 나머지 가능한 경우
    else:
        # B 일의 자리 수가 1이라면
        if B % 10 == 1:
            B //= 10
            cnt += 1
        else:
            B //= 2
            cnt += 1

print(cnt)