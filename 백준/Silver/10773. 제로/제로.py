import sys
input = sys.stdin.readline
num_list = []
cnt = int(input())

for i in range(cnt):
    num = int(input())

    if num != 0:
        num_list.append(num)

    else:
        num_list.pop()
        
print(sum(num_list))