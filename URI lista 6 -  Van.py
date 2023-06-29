while True:
    try:
        nome = []
        dist = []
        regiao = []
        n = int(input())
        
        for _ in range(n):
            van = input().split()
            nome.append(van[0])
            regiao.append(van[1])
            dist.append(int(van[2]))

        #ordenar baseado em Dist
        for i in range(len(dist)-1):
            j = i + 1
            menor = i
            while j < len(dist):
                if dist[j] < dist[menor]:
                    menor = j
                j += 1
            dist[i], dist[menor] = dist[menor], dist[i]
            regiao[i], regiao[menor] = regiao[menor], regiao[i]
            nome[i], nome[menor] = nome[menor], nome[i]
           

        #em caso de distancias forem iguais ordenar por regiao
        for i in range(len(regiao)):
            menor = i
            for prox in range(i+1, len(regiao)):
                if dist[prox] == dist[menor]:
                    if regiao[prox] < regiao[menor]:
                        menor = prox
            dist[i], dist[menor] = dist[menor], dist[i]
            regiao[i], regiao[menor] = regiao[menor], regiao[i]
            nome[i], nome[menor] = nome[menor], nome[i]
        
        #em caso de distancias e regiao forem iguais ordenar por Nome
        for i in range(len(regiao)):
            menor = i
            for prox in range(i+1, len(regiao)):
                if dist[prox] == dist[menor] and regiao[prox] == regiao[menor]:
                    if nome[prox] < nome[menor]:
                        menor = prox
            dist[i], dist[menor] = dist[menor], dist[i]
            regiao[i], regiao[menor] = regiao[menor], regiao[i]
            nome[i], nome[menor] = nome[menor], nome[i]

        for n in nome:
            print(n)

    except EOFError:
        break
