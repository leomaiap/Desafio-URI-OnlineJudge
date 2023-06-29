n, m = map(int, input().split())
while True:
    if n == m == 0:
        print('0 0')
        break
    modulos = []
    numeros = []
    for a in range(n):
        num = int(input())
        numeros.append(num)
        if num >= 0 and num % 2 == 0:
            modulos.append((num % m) + 0.1) #soma se + 0.1 no pares, para ja fazer um criterio de desempate de quem é par e impar tendo mesmo modulo
        elif num % 2 == 0 and num < 0:
            modulos.append(-(num % m) + 0.1) #soma se + 0.1 no pares, para ja fazer um criterio de desempate de quem é par e impar tendo mesmo modulo
        if num >= 0 and num % 2 == 1:
            modulos.append(num % m)
        elif num % 2 == 1 and num < 0:
            modulos.append(-(num % m))   
    
    #ordenar sem criterio de desempate
    for i in range(len(modulos)):
        j = i+1
        menor = i
        while j < len(modulos):
            if modulos[j] < modulos[menor]:
                menor = j
            j += 1
        modulos[i], modulos[menor] = modulos[menor], modulos[i]
        numeros[i], numeros[menor] = numeros[menor], numeros[i]
    
    #ordenar usando os criterios de desempate
    for i in range(len(numeros)):
        menor = i
        for prox in range(i+1, len(numeros)):
            if modulos[prox] == modulos[menor] and numeros[prox] % 2 == 0 and numeros[menor] % 2 == 0:
                if numeros[prox] < numeros[menor]:
                    menor = prox
            if modulos[prox] == modulos[menor] and numeros[prox] % 2 == 1 and numeros[menor] % 2 == 1:
                if numeros[prox] > numeros[menor]:
                    menor = prox
            
        modulos[i], modulos[menor] = modulos[menor], modulos[i]
        numeros[i], numeros[menor] = numeros[menor], numeros[i]
    
    print(f'{n} {m}')
    for p in numeros:
        print(p)

    n, m = map(int, input().split())


    