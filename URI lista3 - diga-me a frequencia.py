analise = []
Ascii = []
contagem = []
contagemordenada = []
indice = 1
while True:
    try:
        entrada = str(input())
        #if len(entrada) == 0: #LINNHA EM BRANCO PARA PARAR
        #    break
        for x in range(0, len(entrada)):
            analise.append(ord(entrada[x]))#Convete cada caractere para ASCII, e coloca em lista analise
        
        analise.sort(reverse=True)#ordena analise decrescente
        Ascii.append(analise[0]) #coloca o primeiro item da lista analise, em lista Ascii (por ser o primeiro não precisa participar do laço)
        contagem.append(analise.count(Ascii[0])) #conta quantos itens do indice 0 de ascii tem em analise, e coloca o resultado na lista contagem
        contagemordenada.append(analise.count(Ascii[0])) #cria uma "cópia" de contagem para futura reordenação
        
        for y in range(1, len(analise)): #fará uma repetição sobre toda lista analise do indice 1 até o final, sendo final o tamanho de analise
            if analise[y] != analise[y-1]: #verifica se o indice atual e o anterior são diferentes, para não colocar "duplicadas" na lista Ascii
                #se forem diferentes então...
                Ascii.append(analise[y])#coloca o valor do caractere Ascii que estava na lista analise, na lista Ascii
                contagem.append(analise.count(Ascii[indice])) #conta quantas vezes aquele ASCII aparececeu em analise, e coloca o resultado da comtagem em contagem
                contagemordenada.append(analise.count(Ascii[indice])) #cria uma "copia" de contagem para futura reordenação
                indice +=1 #aciciona +1 em indice para a lista Ascii, por ela não ter o mesmo length de analise, ela tem uma contagem diferente
        contagemordenada.sort() # ordena a copia de contagem de forma crescente, para não alterar a lista contagem pois se alterada daria problema
        
        for z in range(0, len(contagem)):
            valor = contagem.index(contagemordenada[z]) #localiza o valor de indice z da lista contagemordenada, para ser "procurado" pela funçao .index() em qual indice da lista Ascii e contagem está esse valor contado, achado o valor contado acha o valor do ascii pois estao relacionados um com o outro
            print(Ascii[valor], contagem[valor]) #os indices de Ascci e contagem estão um relacionado ao outro, ou seja o que estiver relacionado por exemplo no indice 3 de Ascii é o valor de indice 3 de contagem
            del Ascii[valor] #os valores são apagados para evitar de serem recontados em caso de houver dois caracteres Ascii com a mesma frequencia
            del contagem[valor]
        print()
        #print(f'Analise {analise}')
        #print(f'Ascii      {Ascii}')
        #print(f'frequencia {contagem}')
        #print(f'ordenado   {contagemordenada}')
        analise = []
        Ascii = []
        contagem = []
        contagemordenada = []
        indice = 1
    except EOFError:
        pass
