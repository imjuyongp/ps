from collections import Counter

def solution(X, Y):
    cx = Counter(X)
    cy = Counter(Y)
    result = []
    for i in range(9,-1,-1):
        result.extend(str(i) * min(cx[str(i)], cy[str(i)]))
    if not result:
        return '-1'
    result.sort(reverse=True)
    if(result[0] == '0'):
        return '0'
    return ''.join(result)