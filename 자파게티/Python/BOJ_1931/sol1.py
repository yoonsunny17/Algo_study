N = int(input())
info = []
for _ in range(N):
    start, end = map(int, input().split())
    info.append([start, end])

# 정렬기준 1. 끝나는 시간의 오름차순
# 정렬기준 2. 시작하는 시간의 오름차순

info.sort(key=lambda x:(x[1], x[0]))

# print(info)
cnt = 1  # 회의 몇개 할 수 있는지 세어 줄 변수
end_time = info[0][1]

for i in range(1, N):
    # 만약 이전의 회의 끝나는 시간이 다음 회의 시작 시간보다 일찍 끝난다면 새로 회의 시작 가능
    if info[i][0] >= end_time:
        cnt += 1
        end_time = info[i][1]

print(cnt)