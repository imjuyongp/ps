def solution(mats, park):
    mats.sort(reverse=True) # 큰 돗자리 순으로 정렬
    for mat in mats:
        for i in range(len(park)): # 행반복
            for j in range(len(park[i])): # 열반복
                if(i+mat <= len(park) and j+mat <= len(park[i])):
                    state = True
                    # 정사각형 검사
                    for r in range(i, i+mat):
                        for c in range(j, j+mat):
                            if(park[r][c] != '-1'):
                                state = False
                    if state:
                        return mat
    return -1
                    