def solution(schedules, timelogs, startday):
    answer = 0
    
    #지정시간 +10분 변환함수
    def limit(x):
        hour = x // 100 # 100으로 나눈 몫이 시
        minute = x % 100
        minute += 10
        if(minute >= 60):
            hour += 1
            minute -= 60
        return (hour*100)+minute
    
    for i in range(len(schedules)): # 0,1,2
        success = True
        for idx, j in enumerate(timelogs[i]):
            today = (startday+idx-1)%7+1
            if(today in [6,7]):
                continue
            if(limit(schedules[i]) < j): # 출근시간을 넘은 경우
                success = False
                break
        if success:
            answer+=1
    
    return answer