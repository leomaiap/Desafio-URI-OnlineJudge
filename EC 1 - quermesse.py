#ler quntidades de numeros por teste, se quantidade for igual a zero pare 
nteste = int(input())
contTeste = 1 #contar número do teste
while nteste != 0:
    #ler o numero do ingresso e "anotar" a ordem de chegada
    ningresso = [] 
    ordem = [] 
    ingresso = input().split()
    for i in range(nteste):
        ningresso.append(int(ingresso[i]))
    for o in range(1,nteste+1):
        ordem.append(o)
    #comparar numero do ingresso com a ordem da chegada, se forem iguais é o vencedor do sorteio
    for c in range(len(ordem)):
        if ordem[c] == ningresso[c]:
            print(f'Teste {contTeste}')
            print(c+1)

    contTeste += 1
    print()
    #print(lista)
    #print(ordem)
    nteste = int(input())
