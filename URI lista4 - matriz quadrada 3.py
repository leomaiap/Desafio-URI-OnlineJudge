matriz = []
while True:
    #ler tamanho da matriz, 0 para
    tamanho = int(input())
    if tamanho == 0:
        break
    
    for linhavazia in range(tamanho):
        matriz.append([])
        for colunavazia in range(tamanho):
            matriz[linhavazia].append(0)
    #print(matriz)
    
    matriz[0][0] = 1 
    #print(matriz)
    for linha in range(0, tamanho):
        if linha >= 1:
            matriz[linha][0] = matriz[linha - 1][0] * 2
        for coluna in range(1, tamanho):
            matriz[linha][coluna] = matriz[linha][coluna -1] * 2

    maiorvalor = len(str(matriz[tamanho-1][tamanho-1]))
    for linha in range(tamanho):
        for coluna in range(tamanho):
            if coluna == 0 and linha > 0:
                print(f'\n{matriz[linha][coluna]:>{maiorvalor}}', end=(' '))
            elif coluna == tamanho-1:
                print(f'{matriz[linha][coluna]:>{maiorvalor}}', end=(''))
            #elif linha == tamanho-1 and coluna == tamanho-1:
               # print('\n')
               # print()
            else:
                print(f'{matriz[linha][coluna]:>{maiorvalor}}', end=(' '))

    #print(matriz)
    print()
    print()
    matriz = []

