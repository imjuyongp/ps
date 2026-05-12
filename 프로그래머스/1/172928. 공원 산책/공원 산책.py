def solution(park, routes):
    answer = []
    startX, startY = 0, 0
    for i in range(len(park)):
        for j in range(len(park[i])):
            if(park[i][j]=='S'):
                startX = i
                startY = j
    
    
    for i in range(len(routes)):
        nx, ny = startX, startY
        move = routes[i].split()
        if(move[0]=='E'):
            for j in range(int(move[1])):
                if(0<=ny+1<len(park[0]) and park[nx][ny+1] != 'X'):
                    ny+=1
                    success = True
                else: 
                    success=False 
                    break
            
        elif(move[0]=='W'):
            for j in range(int(move[1])):
                if(0<=ny-1<len(park[0]) and park[nx][ny-1] != 'X'):
                    ny-=1 
                    success = True
                else: 
                    success=False 
                    break
        elif(move[0]=='N'):
            for j in range(int(move[1])):
                if(0<=nx-1<len(park) and park[nx-1][ny] != 'X'):
                    nx-=1
                    success = True
                else: 
                    success=False 
                    break
        elif(move[0]=='S'):
            for j in range(int(move[1])):
                if(0<=nx+1<len(park) and park[nx+1][ny] != 'X'):
                    nx+=1  
                    success = True
                else: 
                    success=False 
                    break
        if success: 
            startX, startY = nx, ny
    answer = [startX, startY]
    return answer