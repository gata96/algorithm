def solution(a, b, n):
    cnt = 0
    while (n >= a):
        namoji = n % a
        n = (n // a) * b
        cnt += n
        n += namoji
    return cnt
        
        