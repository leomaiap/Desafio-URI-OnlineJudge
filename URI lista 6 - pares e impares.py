n = int(input())
par = []
impar = []
for a in range(n):
    numero = int(input())
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)

#ordenar pares
for i in range(len(par)-1):
    j = i + 1
    menor = i
    while j < len(par):
        if par[j] < par[menor]:
            menor = j
        j += 1
    par[i], par[menor] = par[menor], par[i]

#ordenar impares
for i in range(len(impar)-1):
    j = i + 1
    menor = i
    while j < len(impar):
        if impar[j] > par[menor]:
            menor = j
        j += 1
    impar[i], impar[menor] = impar[menor], impar[i]

for p in par:
    print(p)
for i in impar:
    print(i)