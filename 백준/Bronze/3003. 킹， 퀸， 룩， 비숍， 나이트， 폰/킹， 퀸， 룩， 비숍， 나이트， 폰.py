import sys
input = sys.stdin.readline
n = [1,1,2,2,2,8]
a = list(map(int,input().split()))

for i in range(6):
    print(n[i]-a[i],end = ' ')
