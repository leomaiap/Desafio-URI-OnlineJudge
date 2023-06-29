#ler quanrtidade de testes
teste = int(input())
#ler quantidade de altura a serem digitadas
for x in range(teste):
    quant = int(input())
    alturas = input().split()
    
    #criar lista com 210 casas, casa 0= 20cm, casa 209= 230cm
    quanttamanhos = []
    for z in range(210):
        quanttamanhos.append(0)

    #contar quantas vezes aquela altura apareceu
    for loc in range(quant):
        localizacao = int(alturas[loc]) - 20
        quanttamanhos[localizacao] += 1

    #imprimir quantas vezes altura apareceu de forma ordenada
    c = 0
    for x in range(210):
        if quanttamanhos[x] > 0:
            for p in range(quanttamanhos[x]):
                if c == quant - 1:
                    print(x+20)
                else:
                    print(x+20, end=(' '))
                    c += 1
    