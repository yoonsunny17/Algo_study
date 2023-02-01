n, k = map(int, input().split())
students = list(map(int, input().split()))

arr = []  # 인접한 애들끼리 키 차이 넣어줄 것
for i in range(1, n):
    arr.append(students[i] - students[i-1])

arr.sort(reverse=True)
print(sum(arr[k-1:]))