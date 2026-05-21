def solution(s):
    arr = list(map(int, s.split())) # 공백 기준 자름
    return f"{min(arr)} {max(arr)}"