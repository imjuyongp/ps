def solution(lottos, win_nums):
    correct = 0
    zero_cnt = 0
    win_max = 0
    win_min = 0
    
    def rank(count):
        return min(count, 6)
    
    for i in lottos:
        if i==0:
            zero_cnt += 1
        elif i in win_nums:
            correct += 1
    
    win_max = 7- (correct + zero_cnt)
    win_min = 7 - correct
    
    return [rank(win_max), rank(win_min)]