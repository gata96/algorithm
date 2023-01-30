matrix = []
sum1 = []
for _ in range(5):
    line = list(map(int,input().split()))
    matrix.append(line)
    sum1.append(sum(matrix[_]))
print(sum1.index(max(sum1))+1, max(sum1))

