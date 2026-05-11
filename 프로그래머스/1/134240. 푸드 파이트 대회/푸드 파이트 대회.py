def solution(food):
    answer = ''
    left = ''
    for i, cnt in enumerate(food):
        if(i==0):
            continue
        left += str(i) * (cnt//2)
    answer = str(left) + '0' + str(left[::-1])
    return answer