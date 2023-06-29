sim = []
nao = []
amigo = []
maior = 0
while True:
    inscricao = input().split()
    if inscricao[0] == 'FIM':
        break
    if inscricao[1] == 'YES' and inscricao[0] not in sim:
        sim.append(inscricao[0])
        if len(inscricao[0]) > maior:
            maior = len(inscricao[0])
            amigo.insert(0, inscricao[0])
    elif inscricao[1] == 'NO':
        nao.append(inscricao[0])
    
#ordenar sim
for i in range(len(sim)):
    j = i+1
    menor = i
    while j < len(sim):
        if sim[j] < sim[menor]:
            menor = j
        j += 1
    sim[i], sim[menor] = sim[menor], sim[i]

#ordenar sim
for i in range(len(nao)):
    j = i+1
    menor = i
    while j < len(nao):
        if nao[j] < nao[menor]:
            menor = j
        j += 1
    nao[i], nao[menor] = nao[menor], nao[i]

for s in sim:
    print(s)
for n in nao:
    print(n)
print()
print('Amigo do Habay:')
print(amigo[0])

