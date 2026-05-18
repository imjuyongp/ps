def solution(nums):
    answer = 0
    #dic = {pok : 0 for pok in nums} # 폰켓몬 마리수를 0으로 초기화 
    #for pok in nums: # 폰켓몬 마리 수를 저장
    #    dic[pok] += 1
    #for i, pok in enumerate(dic):
    #    if(i>=len(nums)//2):
    #        break
    #    if(dic[pok]==0):
    #        continue
    #    answer += 1 
    #    dic[pok] -= 1
    
    pok = {} # 종류 저장 딕셔너리
    for i in nums:
        if(i not in pok):
            pok[i] = True
    return min(len(nums)//2, len(pok))     
    #return answer