def solution(s):
    answer = True
    p,y = 0,0
    s = s.lower()
    for i in s:
        if(i == 'p'):
            p += 1
        elif(i == 'y'):
            y += 1
    if(p!=y):
        return False
    else:
        return True