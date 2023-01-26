# 세탁소 사장 동혁
import sys
input = sys.stdin.readline
T = int(input())

for t in range(T):
    num = int(input())
    dollar = [25,10,5,1]
    changes = [0,0,0,0]

    for i in range(4):
        changes[i] += num // dollar[i]
        num %= dollar[i]

    print(*changes)