list_odd = []
for i in range(7):
    nums = int(input())
    if nums %2 == 1:
        list_odd.append(nums)
        
if len(list_odd)==0:
    print(-1)


else:
    print(sum(list_odd))
    print(min(list_odd))
    