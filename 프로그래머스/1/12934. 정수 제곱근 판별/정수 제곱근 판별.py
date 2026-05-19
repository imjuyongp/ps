def solution(n):
    answer = 0
    k = n ** 0.5
    if(k.is_integer()):
        return (k+1) ** 2
    else: 
        return -1