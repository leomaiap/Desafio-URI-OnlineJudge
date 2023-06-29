quantteste = int(input())
for q in range(quantteste):
    quantpiso = int(input())
    andarazul = []
    andarvermelho = []
    for qp in range(quantpiso):
        andar = int(input())
        if andar < 0:
            andarvermelho.append(abs(andar))
        else:
            andarazul.append(andar)
    
    for i in range(len(andarazul)):
        j = i + 1
        menor = i
        while j < len(andarazul):
            if andarazul[j] > andarazul[menor]:
                menor = j
            j += 1
        andarazul[i], andarazul[menor] = andarazul[menor], andarazul[i]

    for i in range(len(andarvermelho)):
        j = i+1
        menor = i
        while j < len(andarvermelho):
            if andarvermelho[j] > andarvermelho[menor]:
                menor = j
            j += 1
        andarvermelho[i], andarvermelho[menor] = andarvermelho[menor], andarvermelho[i]

    maiorA = False
    maiorV = False

    if len(andarvermelho) == 0 and len(andarazul) > 0:
       maiorA = True 
    if len(andarazul) == 0 and len(andarvermelho) > 0:
        maiorV = True

    if len(andarazul) and len(andarvermelho) > 0:
        if andarazul[0] > andarvermelho[0] or andarazul[0] == andarvermelho[0]:
            maiorA = True
        else:
            maiorV = True

    ultimoA = False
    ultimoV = False
    
    parar1 = False
    parar2 = False

    predio = []
    if maiorA:
        predio.append(andarazul[0])
        ultimoA = True
        for p in range(len(andarazul)+len(andarvermelho)):
            for v in range(len(andarvermelho)):
                if andarvermelho[v] < predio[-1] and ultimoA:
                    predio.append(andarvermelho[v])
                    ultimoV = True
                    ultimoA = False
                    break
                if v == len(andarvermelho)-1: 
                    parar1 = True
            for a in range(len(andarazul)):
                if andarazul[a] < predio[-1] and ultimoV:
                    predio.append(andarazul[a])
                    ultimoV = False
                    ultimoA = True
                    break
                if a == len(andarazul)-1:
                    parar2 = True
            if parar1 and parar2:
                break


    if maiorV:
        predio.append(andarvermelho[0])
        ultimoV = True
        for p in range(len(andarazul)+len(andarvermelho)):
            for a in range(len(andarazul)):
                if andarazul[a] < predio[-1] and ultimoV:
                    predio.append(andarazul[a])
                    ultimoV = False
                    ultimoA = True
                    break
                if a == len(andarazul)-1:
                    parar1 = True
            for v in range(len(andarvermelho)):
                if andarvermelho[v] < predio[-1] and ultimoA:
                    predio.append(andarvermelho[v])
                    ultimoV = True
                    ultimoA = False
                    break
                if v == len(andarvermelho)-1:
                    parar1 = True
            if parar1 and parar2:
                break

    
    print(len(predio))