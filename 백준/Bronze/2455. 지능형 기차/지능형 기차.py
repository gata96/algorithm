total = 0
lst = []
while True:
    minus, plus = list(map(int,input().split()))
    total += plus - minus
    lst.append(total)
    if plus == 0:
        break
print(max(lst))