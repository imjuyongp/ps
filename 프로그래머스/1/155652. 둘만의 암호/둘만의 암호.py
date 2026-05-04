def solution(s, skip, index):
    answer = ""
    arr = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
           "w", "x", "y", "z"]
    filtered = [x for x in arr if x not in skip] # skip문자열에 포함되어 있지 않으면 x로 저장

    for i in s:
        find = filtered.index(i)
        answer += filtered[(find+index) % len(filtered)]

    return answer