def solution(n, arr1, arr2):
    answer = []
    a1,a2 = [],[]
    
    
    for i in arr1:
        i = bin(i)[2:].zfill(n)
        a1.append(i)
    for i in arr2:
        i = bin(i)[2:].zfill(n)
        a2.append(i)
    
    for a,b in zip(a1,a2):
        k=""
        for i in range(n):
            if(a[i]=='0' and b[i]=='0'):
                k += " "
            else:
                k+="#"
        answer.append(k)
    
    return answer