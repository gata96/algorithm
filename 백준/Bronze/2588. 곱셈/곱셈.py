import sys
input = sys.stdin.readline

a = int(input())
b = input() #문자열에 인덱스를 취한후 정수형으로 바꿀 수 있다.

print(a*int(b[2]))
print(a*int(b[1]))
print(a*int(b[0]))
print(a*int(b))
