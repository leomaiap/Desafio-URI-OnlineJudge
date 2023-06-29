n = int(input())
cid = 1
while n != 0:
    # ler dados dos imoveis
    somaconsumo = 0
    habitantes = 0
    consumo = []
    for c in range(n):
        imovel = input().split()
        consumo.append([int(imovel[0]), int(imovel[1])//int(imovel[0])])
        habitantes += int(imovel[0])
        somaconsumo += int(imovel[1])
    media = (somaconsumo / habitantes)-0.004
    

    
    for a in range(len(consumo)):
        deletar = []
        if a <= len(consumo)-1:
            for b in range(len(consumo)):
                
                if a != b:
                    if consumo[a][1] == consumo[b][1]:
                        soma = 0
                        soma += consumo[a][0]+consumo[b][0]
                        consumo[a].insert(1, soma)
                        del consumo[a][0]   
                        deletar.append(b)
            if len(deletar) > 0: 
                cont = 0
                for d in deletar:
                    del consumo[d-cont]
                    cont += 1
        else:
            break
    
    for i in range(len(consumo)):
        j = i+1
        menor = i
        while j < len(consumo):
            if consumo[j][1] < consumo[menor][1]:
                menor = j
            j += 1
        consumo[i], consumo[menor] = consumo[menor], consumo[i]
        
    
    print(f'Cidade# {cid}:')
    
    cid += 1
    for x in range(len(consumo)):
        if x != len(consumo)-1:
            print(f'{consumo[x][0]}-{consumo[x][1]}', end=(' '))
        else:
            print(f'{consumo[x][0]}-{consumo[x][1]}')
    print(f'Consumo medio: {media:.2f} m3.')
    print()
    n = int(input())


