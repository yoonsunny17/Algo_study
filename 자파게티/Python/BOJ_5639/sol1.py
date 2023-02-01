import sys
sys.setrecursionlimit(10**9)

numbs = list()
while True:
    try:
        numbs.append(int(sys.stdin.readline()))
    except:
        break

# 후위순회 : left, right, middle
def postorder(start, end):
    if start > end:
        return
    mid = end + 1

    for i in range(start+1, end+1):
        if numbs[start] < numbs[i]:
            mid = i
            break
    
    postorder(start+1, mid-1)  # 왼쪽 트리
    postorder(mid, end)  # 오른쪽 트리
    print(numbs[start])  # 루트 노드

postorder(0, len(numbs)-1)


'''
1. recursion error 방지를 위해 setrecursionlimit 사용
2. try - except 사용하여 입력 있는 동안만 입력 받기
3. 재귀 사용하여 가장 작은 트리부터 확인
4. for문 돌려서 루트(numbs[start])보다 커지면 오른쪽 노드
5-1. [start+1, mid-1] 왼쪽 노드 && [mid, end] 오른쪽 노드로 나누기
5-2. 왼쪽 노드들만 다시 확인(재귀) => 가장 작은 트리까지
6-1. 왼쪽 노드 출력하면 오른쪽 노드 확인하는 함수 확인
6-2. 오른쪽 노드 출력
6-3. 루트 출력
'''