def solution(players,callings):
    # name:idx (선수이름:등수) 딕셔너리 만들기
    dic = {name:idx for idx,name in enumerate(players)}
    
    for name in callings: 
        # 지금 부른 선수의 인덱스를 찾는다.
        idx = dic[name]
        
        # idx를 가진 선수가 idx-1 선수를 추월한다.
        players[idx-1], players[idx] = players[idx], players[idx-1]
        
        # dic에 업데이트하기
        dic[players[idx]] = idx
        dic[players[idx-1]] = idx-1
        
    return players