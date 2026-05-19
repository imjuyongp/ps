def solution(bandage, health, attacks):
    answer = health # 현재 체력
    success = 0 # 연속 성공
    prev = 0 # 이전 공격시간
    for attack in attacks:
        for i in range(attack[0]-prev-1): # 이전 공격시간 부터 다음 공격시간까지 반복
            
            if(answer <= health):
                answer += bandage[1] # 회복 처리
                if(answer>=health):
                    answer = health
            success+=1 # 연속시간 update
            
            # 연속 성공 처리
            if(success == bandage[0]):
                answer+=bandage[2]
                if(answer>=health):
                    answer = health
                success = 0
        # 공격
        answer -= attack[1]
        
        if(answer<=0):
            return -1
        
        success = 0 # 연속 성공 초기화
        prev = attack[0]
    return answer