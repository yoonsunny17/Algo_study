# 스위치 상태 바꾸는 함수 정의해줘
def switching(numb):
    switches[numb] = int(not switches[numb])
    return

N = int(input())  # 스위치 개수
switches = [-1] + list(map(int, input().split()))  # 각 스위치 상태
students = int(input())  # 학생 수

for _ in range(students):
    gender, numb = map(int, input().split())  # 각 학생 성별, 부여받은 번호

    # 남학생인 경우라면,
    if gender == 1:
        for i in range(numb, N+1):
            if i % numb == 0:
                switching(i)

            else:
                continue

    # 여학생의 경우라면,
    if gender == 2:
        # 우선 해당하는 번호의 스위치 상태부터 바꿔주자
        switching(numb)

        # 그 다음에 좌우대칭 스위치 상태 바꿔줄꺼야
        # 체크 횟수는 총 스위치 개수 // 2
        for i in range(1, N//2):
            # 범위 초과하면 멈춰!
            if (numb + i) > N or (numb - i) < 0:
                break

            # 만약 좌우대칭 스위치끼리 상태가 동일하다면
            if switches[numb - i] == switches[numb + i]:
                # 둘 다 상태 바꿔줘!
                switching(numb - i)
                switching(numb + i)
            
            # 바꾸는 도중에 둘이 같은 경우가 아니면 그냥 끝!
            else:
                break

for idx in range(1, N+1):
    print(switches[idx], end=" ")

    # 한 줄에 20개씩 출력해
    if idx % 20 == 0:
        print("")
    