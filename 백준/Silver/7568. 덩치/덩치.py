T = int(input())
lst = []
for t in range(T):
    a, b = list(map(int,input().split()))
    lst.append((a, b))


for i in lst:
    rank = 1
    for j in lst:
        if i[0] != j[0] and i[1] != j[1]:
            if i[0] < j[0] and i[1] < j[1]:
                rank += 1
    print(rank)