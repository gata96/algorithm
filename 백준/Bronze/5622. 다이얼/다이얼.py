alphabet = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
second = 0
saying = input()

for i in range(len(saying)):
    #saying의 각 알파벳이 alphabt내에서 몇번째 인덱스에 속하는지?
    for alpha in alphabet:
        if saying[i] in alpha:
            second += alphabet.index(alpha) +3

print(second)