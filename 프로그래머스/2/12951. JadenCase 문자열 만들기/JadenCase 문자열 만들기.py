def solution(s):
    answer = ''
    state = True # 이전이 공백이면 true
    for c in s:
        if state:
            answer += c.upper()
        else:
            answer += c.lower()
        if c == ' ':   
            state = True
        else: 
            state = False
    return answer