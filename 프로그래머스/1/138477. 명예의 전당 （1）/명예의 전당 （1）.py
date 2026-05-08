import heapq
def solution(k, score):
    answer = []
    top = [] # 명예의 전당
    for s in score:
        if(len(top)<k):
            heapq.heappush(top, s)
        else:
            if min(top) < s:
                heapq.heappushpop(top, s)
        answer.append(min(top))
        
    return answer