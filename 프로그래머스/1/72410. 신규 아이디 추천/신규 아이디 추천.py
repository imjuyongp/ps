def solution(new_id):
    def phase4(s):
        # s and...로 빈 문자열 입력 방지
        if(s and s[0] == '.'):
            s = s[1:] # 첫글자 제거
        if(s and s[-1] == '.'):
            s = s[:-1] # 마지막 글자 제거
        return s
    
    # phase 1
    new_id = new_id.lower()
    
    # phase 2
    result = '' # 허용 문자를 임시 저장
    for i in new_id:
        if(i.isalnum() or i =='-' or i == '_' or i == '.'):
            result += i
    new_id = result # 대체
            
    # phase 3
    # '..'를 '.'로 변환하는 것을 반복
    while '..' in new_id:
        new_id = new_id.replace('..','.')
    
    # phase 4(helper func)
    new_id = phase4(new_id)
            
    # phase 5
    if not new_id:
        new_id += 'a'
        
    # phase 6
    if(len(new_id)>=16):
        new_id = new_id[:15]
    new_id = phase4(new_id)
    
    # phase 7
    if(len(new_id)<=2):
        while(len(new_id)!=3):
            a = new_id[-1]
            new_id += a
    
    return new_id