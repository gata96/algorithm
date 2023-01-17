T = int(input())
total = 0

for t in range(1,T+1):
  count = int(input())
  numbers = list(map(int, input().split()))
  # print(numbers)
  print(sum(numbers))
