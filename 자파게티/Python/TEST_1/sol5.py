from collections import deque

def solution(progresses, speeds):
    n = len(progresses)
    days = []  # 총 며칠 더 일해야 하는지 담을 배열
    for i in range(n):
        rest = 100 - progresses[i]
        
        # 만약에 speed로 나눈 값이 나누어 떨어지면 몫 만큼 일 수 넣어주고
        # 아니면 +1 일 해주기
        if rest % speeds[i] == 0:
            days.append(rest // speeds[i])
        else:
            days.append(rest // speeds[i] + 1)
    
    print(days)
    answer = []
    cnt = 1
    for i in range(len(days)-1):
        if days[i] > days[i+1]:
            cnt += 1
        else:
            answer.append(cnt)
    
    return answer


    cnt=1 # 1개는 무적권 배포하니깐 1
    while(work_flow):
        if cnt > 1 : # 2개 이상 배포시 이미 배포된 부분 pop하면서 cnt를 1로 초기화
            cnt-=1 
            now_progres=work_flow.popleft()
            continue

        now_progres=work_flow.popleft() # 현재프로그레스 pop
        for progres in work_flow : 
            if now_progres >= progres : # 현재 프로그레스랑 비교해서 같거나 작으면 동시배포할거 찾음
                cnt+=1 
            else :  # 다음 프로그레스가 동시배포 안되면 그뒤는 볼필요 없음으로 break
                break
        answer.append(cnt) # 개수를 정답에 저장
    return answer