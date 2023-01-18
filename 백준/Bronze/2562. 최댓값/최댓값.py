num_list= []
for i in range(9):
    num = int(input())
    num_list.append(num)
a = max(num_list)
print(a)
print(num_list.index(a)+1)
