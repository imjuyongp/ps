def solution(dartResult):
    score = []
    answer = 0
    i = 0
    dic = {
        'S' : 1,
        'D' : 2,
        'T' : 3
    }
    
    while i < len(dartResult):
        # 점수 판별
        if dartResult[i] == '1' and i+1 < len(dartResult) and dartResult[i+1] == '0':
            answer = 10
            i += 2
        else:
            answer = int(dartResult[i])
            i += 1
        
        # 점수 계산 + 옵션 판별
        answer **= dic[dartResult[i]] # 보너스 계산
        # *옵션 계산
        if i+1 < len(dartResult) and dartResult[i+1] == '*':
            answer *= 2
            if len(score) > 0: # 이전 점수 중첩 계산
                score[-1] *= 2
            i += 2
            score.append(answer)
        # #옵션 계산
        elif i+1 < len(dartResult) and dartResult[i+1] == '#':
            answer *= -1
            i += 2
            score.append(answer)
        else:
            i += 1
            score.append(answer)
        
            
    return sum(score)