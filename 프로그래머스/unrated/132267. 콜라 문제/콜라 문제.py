def solution(a, b, n):
    cnt = 0
    while (n >= a): # 콜라가 2개 이상인 동안 반복 수행
        namoji = n % a # 나머지 빈병
        n = (n // a) * b # 받을 수 있는 빈병
        cnt += n # 받은 병 카운트
        n += namoji # 나머지 빈병을 다시 더해줌
    return cnt
        
        