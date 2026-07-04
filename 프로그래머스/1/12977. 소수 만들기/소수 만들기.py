def solution(nums):
    hap = 0
    arr = []
    
    # 소수 판별    
    def check(a):
        res = True
        cnt = 0
        for i in range(2, int(a ** 0.5)+1):
            if(a % i == 0):
                res = False
                break
        if res:
            arr.append(a)
    
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                hap = nums[i]+nums[j]+nums[k]
                check(hap)
    return len(arr)
                
