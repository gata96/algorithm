a, b = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
total = A+B
result = 2*len(set(total))-len(total)
print(result)