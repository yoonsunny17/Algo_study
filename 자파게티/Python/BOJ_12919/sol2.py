import sys

def dfs(t):
    if t == S:
        print(1)
        sys.exit()
    
    if len(t) == 0:  # t랑 S 길이 같지 않은데 t가 0이 되어버리면 같지 않은거
        return 0
    
    if t[-1] == 'A':  # 마지막 알파벳이 A라면
        dfs(t[:-1])  # 제거해서 재귀

    if t[0] == 'B':  # 첫번째 알파벳이 B라면
        dfs(t[1:][::-1])  # 제거하고 뒤집어서 재귀

S = list(input())
T = list(input())

dfs(T)  
print(0)  # dfs 돌려서 1 안나오면 0 나올거야