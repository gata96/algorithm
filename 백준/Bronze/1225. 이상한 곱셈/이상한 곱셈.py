import sys
input = sys.stdin.readline
A, B = input().split()
# print(type(A)) # str

A =list(map(int,A)) # int로 바꿔줌
B =list(map(int,B)) # int로 바꿔줌
print(sum(A)*sum(B))
