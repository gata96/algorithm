a, b = list(map(int, input().split()))

# 두개의 자연수 입력 받기
# 사칙연산 출력하기

A = a + b
B = a - b
C = a * b
D = a / b

# 소수점이하의 숫자 버리기(math모듈사용)
import math

print(math.floor(A))
print(math.floor(B))
print(math.floor(C))
print(math.floor(D))