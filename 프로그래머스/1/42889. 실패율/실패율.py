def solution(N, stages):
    answer = []
    dic = {}
    left = len(stages)
    for i in range(1, N+1):
        fail = stages.count(i)
        if fail==0:
            dic[i] = 0
        else:
            dic[i] = fail / left
            left -= fail
    return sorted(dic, key=dic.get, reverse=True)