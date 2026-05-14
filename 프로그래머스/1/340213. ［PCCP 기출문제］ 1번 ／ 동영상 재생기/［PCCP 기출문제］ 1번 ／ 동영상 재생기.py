def solution(video_len, pos, op_start, op_end, commands):
    # mm:ss -> 초 변환 함수
    def change_sec(x): 
        x = x.split(':') 
        return int(x[0]) * 60 + int(x[1])
    # 초 -> mm:ss 변환함수
    def change(x):
        m = x // 60
        s = x % 60
        return f"{m:02d}:{s:02d}"
    
    for command in commands:
        # 이동 전 검사
        if(change_sec(op_start)<=change_sec(pos)<change_sec(op_end)):
                pos = op_end
        #10초 전으로 이동
        if(command == 'prev'):
            if(0<=change_sec(pos)<10):
                pos = '00:00'
            else:
                res = change_sec(pos) - 10
                pos = change(res)
        #10초 후로 이동
        if(command == 'next'):
            if(change_sec(video_len)-10<change_sec(pos)<change_sec(video_len)):
                pos = video_len
            elif(change_sec(pos)+10>change_sec(video_len)):
                pos = video_len
            else: 
                res = change_sec(pos) + 10
                pos = change(res)
        # 이동 후 검사
        if(change_sec(op_start)<=change_sec(pos)<change_sec(op_end)):
                pos = op_end
    
    return pos