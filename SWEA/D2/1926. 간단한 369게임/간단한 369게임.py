a = int(input())
for i in range(1,1+a):
    i = str(i)
    clap = i.count('3') + i.count('6') + i.count('9') # 3,6,9 포함 개수
    
    if clap == 0:
        print(i,end = ' ')
    else:
        print('-'*clap,end = ' ')
    