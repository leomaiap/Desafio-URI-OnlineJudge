times = int(input())
instancia = 1
while times != 0:
    partidas = (times*(times-1)) / 2
    venceu = []
    cestapro = []
    cestacontra = []
    tm = []
    media = []
    for x in range(times):
        cestapro.append([0])
        cestacontra.append([0])
        tm.append(x+1)
    for p in range(int(partidas)):
        placar = input().split()
        x, y, z, w = int(placar[0]), int(placar[1]), int(placar[2]), int(placar[3])
        if y > w:
            venceu.append(x)
        else:
            venceu.append(z)
        #soma cestas a favor
        cestapro[x-1].append(cestapro[x-1][0] + y)
        cestapro[z-1].append(cestapro[z-1][0] + w)
        #soma cestas contra
        cestacontra[z-1].append(cestacontra[z-1][0] + y)
        cestacontra[x-1].append(cestacontra[x-1][0] + w)
        
        cestapro[x-1].pop(0)
        cestapro[z-1].pop(0)
        cestacontra[z-1].pop(0)
        cestacontra[x-1].pop(0)

    mediacesta = []
    #calcular cesta average e somar a pontuação para desempatar(a soma é sempre menor que 1 para nao alterar a pontuacao original)
    for m in range(times):
        if cestacontra[m][0] != 0: 
            media = (cestapro[m][0] / cestacontra[m][0])
            mediacesta.append(media)
        else: #caso o time leve 0 cestas
            media = cestapro[m][0]
            mediacesta.append(media)

    contagem = [] #pontuacao dos times
    for t in range(1,times+1):                                             #para o desempate soma + pontuacao/100 ↓        +          ↓ indice do time/10 
        contagem.append(((venceu.count(t)*2000) + abs(venceu.count(t)-(times-1))*1000) + mediacesta[t-1] + (cestapro[t-1][0]/10000000) + (times-t)/1000000)
    
    for i in range(0, times):
        menor = i
        for prox in range(i+1, times):
            if contagem[prox] > contagem[menor]:
                menor = prox
        contagem[i], contagem[menor] = contagem[menor], contagem[i]
        tm[i], tm[menor] = tm[menor], tm[i]
    
    

    print(f'Instancia {instancia}')
    for p in tm:
        if p == tm[-1]:
            print(p)
        else:
            print(p, end=' ')
    #print()
    print()
    instancia += 1
    times = int(input())


