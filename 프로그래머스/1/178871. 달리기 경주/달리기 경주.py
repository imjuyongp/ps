def solution(players, callings):
    rank = {}
    for i, player in enumerate(players):
        rank[player] = i # 선수이름 : 등수
    
    for call in callings:
        now = rank[call] # 불린 사람의 현재 등수
        front = players[now - 1] # 앞 선수 이름
        
        # 자리 교체
        players[now], players[now-1] = players[now-1], players[now]
        
        rank[call] -= 1
        rank[front] += 1
                
    return players