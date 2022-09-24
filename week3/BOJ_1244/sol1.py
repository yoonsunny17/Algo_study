N = int(input())  # 스위치 개수
switches = [-1] + list(map(int, input().split()))  # 스위치 상태 0, 1
students = int(input())  # 학생 수

# 스위치 상태 바꿔주는 함수 정의해주기
def switching(numb):
    if switches[numb] == 1:
        switches[numb] = 0
    else:
        switches[numb] = 1

# 각 학생 성별, 받은 번호
for _ in range(students):
    gender, numb = map(int, input().split())

    # 남학생인 경우
    if gender == 1:
        for i in range(numb, N+1):
            # 받은 번호의 배수에 해당하는 스위치들의 상태를 바꿔줘
            if i % numb == 0:
                switching(i)

            else:
                continue

    # 여학생인 경우
    elif gender == 2:
        switching(numb)  # 해당 번호 스위치 상태 먼저 바꿔줘
        # 좌우대칭 최대 반복 횟수 = 전체 스위치 개수//2
        for j in range(1, N//2):
            # 범위가 넘어가는 경우 종료
            if (numb + j) > N or (numb - j) < 0:
                break

            # 조건이 충족되는 동안은 상태 계속 바꾸기
            if switches[numb - j] == switches[numb + j]:
                switching(numb + j)
                switching(numb - j)

            else:
                break

for i in range(1, N+1):
    print(switches[i], end=' ')
    if i % 20 == 0:
        print('')