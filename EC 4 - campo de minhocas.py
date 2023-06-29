l, c = map(int, input().split())
minhocas = [None] * l

for lin in range(l):
    minhocas[lin] = list(map(int, input().split()))

maximo = 0

# somar linha por linha
for ll in range(l):
    soma = 0
    for cc in range(c):
        soma += minhocas[ll][cc]
    if soma > maximo:
        maximo = soma

# somar coluna por coluna
for cc in range(c):
    soma = 0
    for ll in range(l):
        soma += minhocas[ll][cc]
    if soma > maximo:
        maximo = soma

print(maximo)