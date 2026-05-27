def solution(a, b):
    res = 0
    for i,j in zip(a,b):
        nz = i * j
        res += nz
    return res