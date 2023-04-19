def solution(name,yearning,photo):
    result = []
    score = 0
    dic = {n:y for n,y in zip(name,yearning)}
    # zip : 튜플 형태로 name과 yearning의 각 원소를 차례로 묶음
    
    # 2중 for문으로 photo의 원소 하나 select
    for pho in photo:
        for p in pho:
            if p in dic.keys(): # 그 원소가 dic의 key값으로 존재하는가?
                score += dic[p] # key값의 value, 즉 점수를 result에 담기
        result.append(score) # score값을 result리스트에 차례로 담아주기
        score = 0 # 0으로 초기화
    
    return result