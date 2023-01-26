import sys
input = sys.stdin.readline

cnt = int(input())
num1 = list(map(int, input().split()))
num2 = set(num1)

print(len(num1)-len(num2))
