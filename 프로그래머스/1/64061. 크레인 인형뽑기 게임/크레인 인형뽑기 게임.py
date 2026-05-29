def solution(board, moves):
    answer = 0
    stack = []
    point = -1
    for i in moves:
        i-=1
        for j in range(len(board[0])):
            if(board[j][i] != 0):
                stack.append(board[j][i])
                point+=1
                board[j][i] = 0
                if(stack[point]==stack[point-1] and len(stack)>=2):
                    stack.pop()
                    stack.pop()
                    point-=2
                    answer+=2
                break
    return answer