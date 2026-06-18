def solution(survey, choices):
    answer = ''
    score = {
        'R':0, 'T':0,
        'C':0, 'F':0,
        'J':0, 'M':0,
        'A':0, 'N':0
    }
    
    for s,c in zip(survey,choices):
        if c < 4 :
            score[s[0]] += 4 - c
        elif c > 4:
            score[s[1]] += c - 4
            
    for a,b in ['RT','CF','JM','AN']:
        if(score[a] >= score[b]):
            answer += a
        else:
            answer += b
    
    return answer