while True:
    try:
        quantidade = int(input())
        a = []
        b = []
        resp = []
        errou = []
        for q in range(quantidade):
            expressao = input()
            expressao = expressao.replace('=', ' ').split()
            a.append(int(expressao[0]))
            b.append(int(expressao[1]))
            resp.append(int(expressao[2]))
        
        for r in range(quantidade):
            resposta = input().split()
            i = int(resposta[1])-1
            if resposta[2] == '+':
                if resp[i] != a[i] + b[i]:
                    errou.append(resposta[0])
            elif resposta[2] == '-':
                if resp[i] != a[i] - b[i]:
                    errou.append(resposta[0])
            elif resposta[2] == '*':
                if resp[i] != a[i] * b[i]:
                    errou.append(resposta[0])
            elif resposta[2] == 'I':
                mult = False
                soma = False
                sub = False
                if resp[i] == a[i] * b[i]:
                    mult = True
                if resp[i] == a[i] + b[i]:
                    soma = True
                if resp[i] == a[i] - b[i]:
                    sub = True
            
                if mult or soma or sub:
                    errou.append(resposta[0])
        
        if len(errou) == 0:
            print('You Shall All Pass!')
        if len(errou) == quantidade:
            print('None Shall Pass!')              
        else:
            for i in range(len(errou)):
                j = i+1
                menor = i
                while j < len(errou):
                    if errou[j] < errou[menor]:
                        menor = j
                    j += 1
                errou[i], errou[menor] = errou[menor], errou[i]

            for n in range(len(errou)):
                if n == len(errou)-1:
                    print(f'{errou[n]}')
                else:
                    print(f'{errou[n]}', end=' ')
            #print()

    except EOFError:
        break
