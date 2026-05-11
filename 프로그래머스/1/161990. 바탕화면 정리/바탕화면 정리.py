def solution(wallpaper):
    answer = []
    min_row=999
    min_col=999
    max_row=0
    max_col=0
    
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                min_row = min(min_row, i)
                min_col = min(min_col, j)
                max_row = max(max_row, i)
                max_col = max(max_col, j)
    answer = [min_row, min_col, max_row+1, max_col+1]
            
    return answer