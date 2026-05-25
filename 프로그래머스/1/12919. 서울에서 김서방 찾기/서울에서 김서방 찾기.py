def solution(seoul):
    answer = ''
    for idx,ch in enumerate(seoul):
        if(ch == "Kim"):
            return f"김서방은 {idx}에 있다"
        