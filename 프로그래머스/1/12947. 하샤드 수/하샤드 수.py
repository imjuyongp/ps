def solution(x):
    arr=list(map(int,str(x)))
    sum = 0
    for i in arr:
        sum+=i
    if(x%sum==0):
        return True
    return False