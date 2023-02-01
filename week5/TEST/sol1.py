part_times = [[1,10,10],[4,7,18],[2,3,9],[3,5,7],[1,4,3],[10,19,19]]

visited = [0] *  len(part_times)


flag = 0


rlt = []

def makeList(a,b):
    return [ x for x in range(a,b+1)]

def check(check,numList):
    for ch in check:
        if ch in numList:
            return False
    return True

def dfs(partTime,idx):
    global flag,total,numList

    if flag == 1:
        return
    
    checkNumList = makeList(partTime[0]+1,partTime[1])
    
    if check(checkNumList,numList):
        numList += checkNumList
        total += partTime[2]
        numList.sort()


    if idx == len(partTime):
        flag = 1
        rlt.append(total)
        return
    
    
    for j in range(len(part_times)):
        if visited[j] == 0:
            visited[j] = 1
            dfs(part_times[j],idx+1)
            visited[j] = 0

for i in range(len(part_times)):
    flag = 0
    total = part_times[i][2]
    if visited[i] == 0:
        visited[i] = 1
        numList = makeList(part_times[i][0],part_times[i][1])
        dfs(part_times[i],0)
        visited[i] = 0
print(max(rlt))