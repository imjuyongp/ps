def solution(today, terms, privacies):
    answer = []
    dict = {} # 약관종류와 보관기관 딕셔너리
    
    # 날짜를 일로 반환하는 함수
    def changeDate(todays):
        y,m,d = map(int, todays.split('.'))
        return y*12*28+m*28+d
    
    date_today = changeDate(today) # 현재 날짜 일로 변경
    
    # 약관 정보 딕셔너리에 저장
    for t in terms:
        res = t.split()
        dict[res[0]] = int(res[1])*28 # 약관 보관일을 일로 저장
        res = []
        
    for i,p in enumerate(privacies):
        pri = p.split()
        pri_date = changeDate(pri[0]) # 저장시간 일로 변환
        if(date_today >= pri_date+int(dict[pri[1]])):
            answer.append(i+1)
        
    return answer