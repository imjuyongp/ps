def solution(absolutes, signs):
    answer = []
    for i in range(len(signs)):
        if(signs[i]):
            signs[i]=1
        else:
            signs[i]=-1
        answer.append(absolutes[i]*signs[i])
        
    return sum(answer)