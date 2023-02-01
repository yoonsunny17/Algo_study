import sys

def binarySearch(target, left, right):
    while left <= right:
        mid = (left + right) // 2

        if target == cards[mid]:
            return cards[mid]
        
        elif target > cards[mid]:
            return binarySearch(target, mid+1, right)
        
        else:
            return binarySearch(target, left, mid-1)

    return None

n = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
cards.sort()  # 오름차순 정렬
m = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

left = 0
right = n-1

for i in arr:
    print(cards.count(i), end=' ') if binarySearch(i, left, right) is not None else print(0, end=' ')