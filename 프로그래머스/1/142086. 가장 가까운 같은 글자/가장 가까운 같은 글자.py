def solution(s):
    answer = []
    dic = {}
    for i,ch in enumerate(s):
        res = 0
        if(ch not in dic):
            dic[ch] = i
            answer.append(-1)
        else: 
            res = i - dic[ch]
            answer.append(res)
            dic[ch] = i
        
    return answer