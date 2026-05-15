def solution(n):
    answer = 0
    ch = str(n)
    for i in range(len(ch)):
        answer += int(ch[i])
    
    return answer