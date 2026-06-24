def solution(answers):
    result = []
    pn = len(answers) # 문제수
    p1 = [1,2,3,4,5] # 5
    p2 = [2,1,2,3,2,4,2,5] # 8
    p3 = [3,3,1,1,2,2,4,4,5,5] # 10
    score = [0,0,0]
    
    for i in range(pn):
        if(answers[i] == p1[i%5]):
            score[0] += 1
        if(answers[i] == p2[i%8]):
            score[1] += 1
        if(answers[i] == p3[i%10]):
            score[2] += 1
            
    max_score = max(score)
    
    return [idx+1 for idx, c in enumerate(score) if (c == max_score)]