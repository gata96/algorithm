total = int(input())
N = int(input())
total_price= 0

for i in range(N):
  price, count = list(map(int,input().split()))
  total_price += price * count

if total == total_price:
  print('Yes')

else:
  print('No')