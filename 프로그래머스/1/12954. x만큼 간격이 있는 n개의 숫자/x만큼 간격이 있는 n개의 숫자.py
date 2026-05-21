def solution(x, n):
    answer = []
    for i in range(n):
        new = x * (i+1)
        answer.append(new)
    return answer