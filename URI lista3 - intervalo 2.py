n = int(input())
valores = []
In = 0
out = 0
for c in range(n):
    valores.append(int(input()))
indice = 0
for d in range(n):
    if 10 <= valores[indice] <= 20:
        if -10000000 < valores[indice] < 10000000:
            In += 1
        else:
            out += 1
    else:
        out += 1
    indice += 1
print('{} in'.format(In))
print('{} out'.format(out))
