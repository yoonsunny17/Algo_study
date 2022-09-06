# i = 연산자 몇 번 사용했는지 확인해주는 변수
def dfs(i, rlt, add, sub, mlt, div):
    global max_rlt, min_rlt

    # 종료 조건 = 연산 반복을 N-1번 끝냈다면, 결과값 갱신 후 반환해줘
    if i == N:
        max_rlt = max(max_rlt, rlt)
        min_rlt = min(min_rlt, rlt)
        return

    # 네개의 연산자에 대해 동일한 과정을 반복해줄거야
    # 만약에 아직 사용하지 않은 연산자의 개수가 1개 이상이라면 -1씩 감소시켜주고,
    # rlt값 계산해주고
    # dfs 재귀 호출해서 다음 연산으로 넘어가자
    if add > 0:
        dfs(i+1, rlt+numbs[i], add-1, sub, mlt, div)
    if sub > 0:
        dfs(i+1, rlt-numbs[i], add, sub-1, mlt, div)
    if mlt > 0:
        dfs(i+1, rlt*numbs[i], add, sub, mlt-1 ,div)
    # rlt가 음수인 경우, 양수인 경우 2가지 고려해야 함!
    if div > 0:
        dfs(i+1, -((-rlt)//numbs[i]) if rlt < 0 else (rlt//numbs[i]), add, sub, mlt, div-1)


N = int(input())
numbs = list(map(int, input().split()))  # N개의 숫자
ops = list(map(int, input().split()))  # 덧셈, 뺄셈, 곱셈, 나눗셈 개수

# 최댓값, 최솟값 초기화 (처음에는 값 반대로)
max_rlt = -10**9
min_rlt = 10**9

# 무조건 연산자 처음에 1번 사용하면서 시작하는거니까 i = 1 부터 시작 
dfs(1, numbs[0], ops[0], ops[1], ops[2], ops[3])

print(f'{max_rlt}\n{min_rlt}')