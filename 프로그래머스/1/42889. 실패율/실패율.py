def solution(N, stages):
    answer = []
    dic = {}
    left = len(stages)
    
    for stage in range(1, N+1):
        fail = stages.count(stage)
        if fail == 0:
            dic[stage] = 0
        else:
            dic[stage] = fail/left
            left -= fail
    
    answer = sorted(dic, key=dic.get, reverse=True)
            
    
    return answer