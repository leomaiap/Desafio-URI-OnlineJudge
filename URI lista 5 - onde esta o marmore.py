#ler entrada de N (quantidades de marmores)e Q (numero de consultas)
#se ambos forem iguais a zero pare
caso = 1
while True:
    nq = input().split()
    n, q = int(nq[0]), int(nq[1])
    if n == q == 0:
        break
    #ler n vezes valor dos marmores, e colocar em ordem
    marmores = []
    for a in range(n):
        marmores.append(int(input()))
    
    for i in range(len(marmores)):
        j = i + 1
        menor = i
        while j < len(marmores):
            if marmores[j] < marmores[menor]:
                menor = j
            j += 1
        marmores[i], marmores[menor] = marmores[menor], marmores[i]

    #imprimir numero do caso
    print(f'CASE# {caso}:')
    #caso é incrementado
    caso+=1
    #ler q vezes valor da consulta, e informar o incice no qual ele se encontra,se não achar dizer que nao achou 
    for b in range(q):
        numero = int(input())
        encontrado = False
        for i in range(len(marmores)):
            if numero == marmores[i]:
                print(f'{numero} found at {i+1}')
                encontrado = True
                break
        if encontrado == False:
            print(f'{numero} not found')
