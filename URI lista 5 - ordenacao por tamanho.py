#ler quantidades de testes
teste = int(input())
for t in range(teste):
    strings = input().split()
    #medir tamanho das palavras
    tamanho = []
    for x in range(len(strings)):
        tamanho.append(len(strings[x]))
    #ordenar tamanho das palavras, associar numeros as palavras
    for i in range(len(strings)):
        pos = i
        while pos > 0:
            if tamanho[pos-1] < tamanho[pos]:
                tamanho[pos-1], tamanho[pos] = tamanho[pos], tamanho[pos-1]
                strings[pos-1], strings[pos] = strings[pos], strings[pos-1]
            pos -= 1
    #imprimir a resposta
    for r in range(len(strings)):
        if r == len(strings)-1:
            print(f'{strings[r]}')            
        else:
            print(f'{strings[r]}', end=(' '))