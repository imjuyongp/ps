def solution(s):
    answer, same, diff, point = 0,0,0,0
    for idx, i in enumerate(s):
        if i == s[point]:
            same += 1
        else:
            diff += 1
        if same == diff:
            answer += 1
            point = idx+1
            same, diff = 0,0
    if same != 0 or diff != 0:
        answer+= 1
    return answer