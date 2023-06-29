while True:
    try:
        nm = input().split()
        numLinha = int(nm[0])
        numColuna = int(nm[1])
        matriz = []
        for linhavazia in range(numLinha):
            matriz.append([])
        for l in range(numLinha):
            linha = input().split()
            for c in range(numColuna):
                matriz[l].append(int(linha[c]))
        
        for l in range(numLinha):
            for c in range(numColuna):
                if matriz[l][c] == 1:
                    jogadorY = l
                    jogadorX = c
                if matriz[l][c] == 2:
                    monstroY = l
                    monstroX = c

        distancia = abs(jogadorY - monstroY) + abs(jogadorX - monstroX)
        print(distancia)

    except EOFError:
        break