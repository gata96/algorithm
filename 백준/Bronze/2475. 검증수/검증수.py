A = list(map(int,input().split()))
total = 0
for i in A:
    total += i**2

print(total%10)