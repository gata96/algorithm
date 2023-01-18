N = int(input())
list_num =[]

for i in range(N):
    num = int(input())
    list_num.append(num)
    
    new = sorted(list_num)

print(*new,sep = '\n')
