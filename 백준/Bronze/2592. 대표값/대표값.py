import sys
import statistics
# sys.stdin = open('input.txt', 'rt')
input = sys.stdin.readline

lst = []
for i in range(10):
    N = int(input().strip())
    lst.append(N)
print(statistics.mean(lst))
print(statistics.mode(lst))