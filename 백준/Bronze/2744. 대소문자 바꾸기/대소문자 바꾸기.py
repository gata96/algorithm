A = input()
for i in A:
    if i.isupper():
        i = i.lower()
    else:
        i = i.upper()
    print(i,end= '')