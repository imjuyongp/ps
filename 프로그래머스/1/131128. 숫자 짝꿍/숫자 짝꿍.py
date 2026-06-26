def solution(X, Y):
    result = []
    for i in range(9,-1,-1):
        result.extend(str(i) * min(X.count(str(i)), Y.count(str(i))))
    if not result:
        return '-1'
    result.sort(reverse=True)
    if(result[0] == '0'):
        return '0'
    return ''.join(result)