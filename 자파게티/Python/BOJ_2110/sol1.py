'''
사실 잘 이해 안됨 이 문제 ..
'''
import sys

def binarySearch(arr, start, end):
    global rlt
    while start <= end:
        mid = (start + end) // 2
        current = arr[0]  # 현재 좌표 위치
        cnt = 1  # 현재 설치한 공유기 개수

        for i in range(1, len(arr)):
            if arr[i] >= current + mid:
                cnt += 1
                current = arr[i]

        # 현재 설치한 공유기 개수가 설치할 수 있는 공유기 개수보다 많으면
        if cnt >= c:
            start = mid + 1
            rlt = mid

        # 현재 설치한 공유기 개수가 설치할 수 있는 공유기 개수보다 적으면
        else:
            end = mid - 1

n, c = map(int, sys.stdin.readline().split())
arr = list(int(sys.stdin.readline()) for _ in range(n))
arr.sort()

start = 1  # 최소 거리
end = arr[-1] - arr[0]  # 최대 거리
rlt = 0
binarySearch(arr, start, end)

print(rlt)