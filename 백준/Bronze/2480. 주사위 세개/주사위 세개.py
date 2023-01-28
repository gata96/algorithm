num = list(map(int, input().split()))
cnt = len(list(set(num)))
if cnt == 1:
    print(10000 + num[0]*1000)

elif cnt == 3:
    print(max(num)*100)

else:
    num.remove(max(num))
    num.remove(min(num))
    print(1000 + num[0]* 100)