#ler N(quantidade de postos intermediarios) M(distancia intermediaria do altleta)
nm = input().split()
n, m = int(nm[0]), int(nm[1])
#ler localizacao dos N postos
locpos = input().split()
posto = []
for p in locpos:
    posto.append(int(p))

sim = True
#verificar se ultimo posto esta dentro da distancia ate a linha de chegada
if (42195 - posto[-1]) > m:
    sim = False
#verificar distancias entre cada posto se são menores ou iguais a M(distancia intermediaria)
if sim == True: #se o ultimo posto esta fora da distancia ignore o laço
    for v in range(1, n):
        if posto[v]-posto[v-1] > m:
            sim = False
            break
#mostrar resultado S se for true N se for False
if sim == True:
    print('S')
else:
    print('N')