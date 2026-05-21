def solution(n):
    arr = []
    for i in range(n):
        if(n%(i+1) == 1):
            arr.append(i+1)
    return min(arr)