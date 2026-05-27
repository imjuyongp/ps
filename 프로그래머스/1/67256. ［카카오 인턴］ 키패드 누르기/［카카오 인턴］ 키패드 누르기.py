def solution(numbers, hand):
    answer = ''
    
    # 거리계산 함수
    def distance(a,b):
        dis = abs(a[0]-b[0]) + abs(a[1]-b[1])
        return dis
    
    board = {
        1:(0,0), 2:(0,1), 3:(0,2),
        4:(1,0), 5:(1,1), 6:(1,2),
        7:(2,0), 8:(2,1), 9:(2,2),
        '*':(3,0), 0:(3,1), '#':(3,2)
    }
    
    # 시작 좌표
    left = board['*']
    right = board['#']
    
    left_col = {1,4,7}
    right_col = {3,6,9}
    
    for i in numbers:
        target = board[i] # 해당 숫자의 좌표
        
        if i in left_col:
            answer+='L'
            left = target
        elif i in right_col:
            answer+='R'
            right = target
            
        else: # 2,5,8,0 처리
            # 거리 저장
            ld = distance(left,target)
            rd = distance(right,target)
            if(ld < rd):
                answer+='L'
                left = target
            elif(ld > rd):
                answer+='R'
                right = target
            else:
                if(hand=='left'):
                    answer+='L'
                    left=target
                else:
                    answer+='R'
                    right=target
    return answer