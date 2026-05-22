def solution(s):
    rm,bn = 0,0
    
    while(s !='1'):
        rm += s.count('0') # 제거할 0의 개수
        s = s.replace('0','') # 0 제거
        s = bin(len(s))[2:] # 2진수 변환
        bn+=1
    
    return [bn,rm]