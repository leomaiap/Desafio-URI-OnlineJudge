x = int(input())
y = int(input())
soma = 0
for c in range(y+1, x):
    if c % 2 == 1:
        soma += c
print(soma)