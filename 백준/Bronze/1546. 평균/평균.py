import statistics
import sys
input = sys.stdin.readline
lst = []
T = int(input())
nums = list(map(int,input().split()))

for i in nums:
    each = (i/max(nums))*100
    lst.append(each)
    total = round(statistics.mean(lst),6)
    # total = round(numpy.mean(lst),6)
print(total)
