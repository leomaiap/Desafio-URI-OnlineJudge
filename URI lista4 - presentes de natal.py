#ler quantidade de netos
# se netos for = 0, parar o loop
#ler valores dos presentes
#adicionar valor dos presentes em uma lista
while True:
    listadevalores = []
    listaordenada = []
    neto = int(input())
    if neto == 0:
        break
    valor =  input().split()
    
    for x in range(len(valor)):
        listadevalores.append(int(valor[x]))
    listaordenada = listadevalores[:]
#criar uma lista ordenada
    listaordenada.sort()
#achar o par mais caro (soma maior valor + menor valor)  
    caro = listaordenada[0] + listaordenada[-1]
    for y in range(neto, 1,-1):
        calculo = listaordenada[neto+y] + listaordenada[neto-1-y]
        if calculo > caro:
            caro = calculo
#achar o par mais barato (acha o "meio" da lista e soma os dois itens)
    barato = listaordenada[neto] + listaordenada[neto-1]
    for y in range(1,neto):
        calculo = listaordenada[neto+y] + listaordenada[neto-1-y]
        if calculo < barato:
            barato = calculo
    valorOrganizado = []
    valorOrganizado.append(barato)
    valorOrganizado.append(caro)
    valorOrganizado.sort()
    #print(caro)
    #print(barato)
    #print(listadevalores)
    #print(listaordenada)
    print(f'{valorOrganizado[1]} {valorOrganizado[0]}')

#'99 91 | 87 83 | 71 65 | 53 47 | 41 33 | 31 30 | 25 21 | 19 17 | 11 9 | 7 5 | 3 1'
 #   '1      2       3       4        5     *        5      4     3      2      1'
