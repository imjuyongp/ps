def solution(keymap, targets):
    answer = []
    char = {}
    
    for key in keymap:
        for i, ch in enumerate(key):
            if(ch in char):  
                char[ch] = min(char[ch], i+1)
            else:
                char[ch] = i+1
    for t in targets:
        total = 0
        for i in t:
            if(i not in char):
                total = -1
                break
            total += char[i]
            
        answer.append(total)
            
    return answer