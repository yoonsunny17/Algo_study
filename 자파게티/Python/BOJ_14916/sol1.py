n = int(input())

cnt = 0

while True:
    # 돈이 5의 배수인 경우 동전 개수 더해주고 끝
    if n % 5 == 0:
        cnt += n // 5
        break

    # 5로 나누어지지 않는 경우라면
    else:
        # 2원씩 빼면서 나누어지는 것이 나오도록
        n -= 2
        cnt += 1

    # 음수인 경우 = 거슬러 줄 수 없는 경우
    if n < 0:
        break

print(-1) if n < 0 else print(cnt)