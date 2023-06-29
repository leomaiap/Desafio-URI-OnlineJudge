#ler a entrada, primeiro item da linha é a quantidade de testes
#se for 0 pare
entrada = input().split()
teste = int(entrada[0])
while teste != 0:
    num = []
    numOrd = []
    for a in range(1, teste+1): #colocar numeros em uma lista
        num.append(int(entrada[a]))
            
    for b in range(1, teste+1):
        numOrd.append(b)
    contagem = 0
    #enquanto todos numeros nao tiverem ordenado faca: #fazer todas ordenacoes possiveis(só pode ordenar se par for A>B)
    while num != numOrd: 
        for i in range(0, len(num)-1): #fazer todas ordenacoes possiveis
            if num[i] > num[i+1]: # Anlisar o par, se A>B, A troca com B
                num[i], num[i+1] = num[i+1], num[i]
                contagem += 1 #conta quantas reordenações tiveram
    
    #como Marcelo é sempre o primeiro a jogar, entao se a quantidade de reordenacoes forem
    #impares Marcelo ganha... Se for par Carlos ganha
    if contagem % 2 == 1:
        print('Marcelo')
    else:
        print('Carlos')
        
    entrada = input().split()
    teste = int(entrada[0])

