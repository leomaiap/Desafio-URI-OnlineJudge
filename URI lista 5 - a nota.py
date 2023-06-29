while True:
    try:
        #ler entradas, N(quantidade nota a serem registradas), K(K-ésimo termos)
        nk = input().split()
        n, k = int(nk[0]), int(nk[1])
        notas = input().split()
        notasord = []
        #colocar notas em lista
        for a in range(n):
            notasord.append(int(notas[a]))
        #ordenar lista
        notasord.sort(reverse=True)
        #Somar os K-ésimos maiores termos
        soma = 0
        for s in range(0, k):
            soma += notasord[s]
        print(soma)
    except EOFError:
        break