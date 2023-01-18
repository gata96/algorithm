T = int(input())

for t in range(1, T+1):
  saying = input().split(' ') # == saying = list(input().split()) # list

  for say in saying:
    print(say[::-1], end = ' ')