n = int(input())
pais = []
o = []
p = []
b = []
for m in range(n):
    medalha = input().split()
    pais.append(medalha[0])
    o.append(int(medalha[1]))
    p.append(int(medalha[2]))
    b.append(int(medalha[3]))

#ordenar baseado em Ouro
for i in range(len(o)-1):
    j = i + 1
    menor = i
    while j < len(o):
        if o[j] > o[menor]:
            menor = j
        j += 1
    o[i], o[menor] = o[menor], o[i]
    p[i], p[menor] = p[menor], p[i]
    b[i], b[menor] = b[menor], b[i]
    pais[i], pais[menor] = pais[menor], pais[i]

#em caso de empate em ouro ordenar empatados por Prata
for i in range(len(p)):
    menor = i
    for prox in range(i+1, len(p)):
        if o[prox] == o[menor]:#se ouro for igual, ordenar por prata
            if p[prox] > p[menor]:
                menor = prox
    o[i], o[menor] = o[menor], o[i]
    p[i], p[menor] = p[menor], p[i]
    b[i], b[menor] = b[menor], b[i]
    pais[i], pais[menor] = pais[menor], pais[i]

#em caso de empate em ouro e prata ordenar empatados por bronze
for i in range(len(b)):
    menor = i
    for prox in range(i+1, len(b)):
        if o[prox] == o[menor] and p[prox] == p[menor]:#se ouro e prata for igual, ordenar por bronze
            if b[prox] > b[menor]:
                menor = prox
    o[i], o[menor] = o[menor], o[i]
    p[i], p[menor] = p[menor], p[i]
    b[i], b[menor] = b[menor], b[i]
    pais[i], pais[menor] = pais[menor], pais[i]

#em caso de empate em ouro e prata e bronze ordenar empatados por Ordem alfabetica do nome do pais
for i in range(len(pais)):
    menor = i
    for prox in range(i+1, len(pais)):
        if o[prox] == o[menor] and p[prox] == p[menor] and b[prox] == b[menor]:
            if pais[prox] < pais[menor]:
                menor = prox
    o[i], o[menor] = o[menor], o[i]
    p[i], p[menor] = p[menor], p[i]
    b[i], b[menor] = b[menor], b[i]
    pais[i], pais[menor] = pais[menor], pais[i]

for m in range(len(pais)):
    print(f'{pais[m]} {o[m]} {p[m]} {b[m]}')
