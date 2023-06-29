valorMoedas = []
#LAÇO while
#ler quantidade de moedas
    #LAÇO - ler x valores de cada moeda, colocar em lista
#ler valor do salto
while True:
    try:
        quantidade = int(input())
        for x in range(0, quantidade):
            entrada = int(input())
            valorMoedas.append(entrada)
        salto = int(input())
        
        soma = 0
        
        for y in range(0, quantidade, salto):
            soma += valorMoedas[y]
                
        #verificar se soma é primo
        resto0 = 0
        for z in range(1, soma+1):
            divisao = soma % z
            if divisao == 0:
                resto0 += 1
        if resto0 == 2:
            print('You’re a coastal aircraft, Robbie, a large silver aircraft.')
        else:
            print('Bad boy! I’ll hit you.')
        valorMoedas = []
        #print(soma)
        #soma = 0
        #resto0 = 0
    except EOFError:
        break