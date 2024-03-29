def get_cds(number, limit , power):
    cnt = 0
    for i in range(1,int(number**(1/2))+1):
        if number % i == 0:
            if i == number**(1/2):
                cnt += 1
            else:
                cnt += 2
        if cnt > limit:
            return power
    return cnt

def solution(number, limit , power):
    total = 0
    for i in range(1,number+1):
        count = get_cds(i, limit , power)
        total += count
        
    return total



    
