#ler quantidade de testes
teste = int(input())
for t in range(teste):
    #ler quantidade alunos, e de notas
    alunos = int(input())
    n = input().split()
    notas = []
    notasOrdenado = []
    for a in range(alunos):
        #colocar notas em listas
        notas.append(int(n[a]))
        notasOrdenado.append(int(n[a]))
    
    #ordenar notas para comaparação
    for i in range(alunos):
        pos = i
        while pos > 0:
            if notasOrdenado[pos-1] < notasOrdenado[pos]:
                notasOrdenado[pos-1], notasOrdenado[pos] = notasOrdenado[pos], notasOrdenado[pos-1]
            pos -= 1
    #print(notasOrdenado)
    
    #comparar listas e contar quais não trocaram de posicao
    naotrocou = 0
    for c in range(alunos):
        if notas[c] == notasOrdenado[c]:
            naotrocou += 1
    print(naotrocou)
