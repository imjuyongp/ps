def solution(k, score):
    answer = []
    top = [] # 명예의 전당
    for s in score:
        if(len(top)<k):
            top.append(s)
        else:
            if min(top) < s:
                top.append(s)
                top.remove(min(top))
        answer.append(min(top))
        
    return answer