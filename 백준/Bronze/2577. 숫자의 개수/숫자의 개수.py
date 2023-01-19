from collections import Counter

A = int(input())
B = int(input())
C = int(input())
total = list(str(A*B*C)) 
for i in range(10):
    print(total.count(str(i)))# str으로 바꾼이유 : count가 문자밖에 인식을 못하기 때문

    