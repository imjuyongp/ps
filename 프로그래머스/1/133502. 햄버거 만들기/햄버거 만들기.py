def solution(ingredient):
    answer = 0
    stack = [] # 1,2,3,1
    
    for i in ingredient:
        stack.append(i)
        if len(stack) >= 4:
            if(stack[-4:] == [1,2,3,1]):
                answer += 1
                del stack[-4:]

    return answer