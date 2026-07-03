def solution(s):
    answer = []
    
    while s:
        first = s[0] # 첫번째 글자
        same = 0
        diff = 0
        for idx, i in enumerate(s):
            if(i == first):
                same += 1
            else:
                diff += 1
            if(same == diff):
                left = s[:idx+1]
                answer.append(left)
                s = s[idx+1:]
                break
        else:
            answer.append(s)
            break
                
    return len(answer)