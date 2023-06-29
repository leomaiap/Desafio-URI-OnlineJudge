#ler numero de casos
#ler quantidade de Renas e quantidade de Renas selecionadas (na mesma linha)

n =  int(input())

for c in range(n):
    rena = []
    peso = []
    idade = []
    altura = []
    quantrenas = input().split()
    qr, sr = int(quantrenas[0]), int(quantrenas[1])
    for a in range(qr):
        dadosrena = input().split()
        rena.append(dadosrena[0])
        peso.append(int(dadosrena[1]))
        idade.append(int(dadosrena[2]))
        altura.append(float(dadosrena[3]))

    #ordenar renas por critério de peso crescente
    for i in range(len(peso)-1):
        j = i + 1
        menor = i
        while j < len(peso):
            if peso[j] > peso[menor]:
                menor = j
            j += 1
        peso[i], peso[menor] = peso[menor], peso[i]
        idade[i], idade[menor] = idade[menor], idade[i]
        altura[i], altura[menor] = altura[menor], altura[i]
        rena[i], rena[menor] = rena[menor], rena[i]
    
    #se pesos forem iguais desempatar por menor idade
    for i in range(len(idade)):
        menor = i
        for prox in range(i+1, len(idade)):
            if peso[prox] == peso[menor]:
                if idade[prox] < idade[menor]:
                    menor = prox
        peso[i], peso[menor] = peso[menor], peso[i]
        idade[i], idade[menor] = idade[menor], idade[i]
        altura[i], altura[menor] = altura[menor], altura[i]
        rena[i], rena[menor] = rena[menor], rena[i]
        
    #se pesos e idade forem iguais desempatar por menor altura
    for i in range(len(altura)):
        menor = i
        for prox in range(i+1, len(altura)):
            if peso[prox] == peso[menor] and idade[prox] == idade[menor]:
                if altura[prox] < altura[menor]:
                    menor = prox
        peso[i], peso[menor] = peso[menor], peso[i]
        idade[i], idade[menor] = idade[menor], idade[i]
        altura[i], altura[menor] = altura[menor], altura[i]
        rena[i], rena[menor] = rena[menor], rena[i]
    
    #se pesos e idade ealtura forem iguais desempatar por Nome
    for i in range(len(rena)):
        menor = i
        for prox in range(i+1, len(rena)):
            if peso[prox] == peso[menor] and idade[prox] == idade[menor] and altura[prox] == altura[menor]:
                if rena[prox] < rena[menor]:
                    menor = prox
        peso[i], peso[menor] = peso[menor], peso[i]
        idade[i], idade[menor] = idade[menor], idade[i]
        altura[i], altura[menor] = altura[menor], altura[i]
        rena[i], rena[menor] = rena[menor], rena[i]
    
    print('CENARIO','{'+f'{c+1}'+'}')
    for r in range(sr):
        print(f'{r+1} - {rena[r]}')
    


