t = int(input()) #numero de casos
for q in range(t): #quantidade de presentes 
    n, k = map(int, input().split())
    iD = []
    vol = []
    for d in range(n): #dimensoes
        ids, alt, lar, pro = map(int, input().split())
        iD.append(ids)
        vol.append(alt*lar*pro)

    #ordenar por volumes
    for i in range(len(vol)):
        j = i+1
        menor = i
        while j < len(vol):
            if vol[j] > vol[menor]:
                menor = j
            j += 1
        vol[i], vol[menor] = vol[menor], vol[i]
        iD[i], iD[menor] = iD[menor], iD[i]

    #ordenar volume iguais pelo menor iD
    for i in range(len(iD)):
        menor = i
        for prox in range(i+1, len(iD)):
            if vol[prox] == vol[menor]: 
                if iD[prox] < iD[menor]:
                    menor = prox            
        vol[i], vol[menor] = vol[menor], vol[i]
        iD[i], iD[menor] = iD[menor], iD[i]
    
    preseteescolhido = []
    preseteescolhido.append(iD[:k])

    for i in range(k):
        j = i+1
        menor = i
        while j < k:
            if preseteescolhido[0][j] < preseteescolhido[0][menor]:
                menor = j
            j += 1
        preseteescolhido[0][i], preseteescolhido[0][menor] = preseteescolhido[0][menor], preseteescolhido[0][i]

    for p in range(k):
        if p == k-1:
            print(preseteescolhido[0][p])
        else:
            print(preseteescolhido[0][p], end=(' '))

    print()
