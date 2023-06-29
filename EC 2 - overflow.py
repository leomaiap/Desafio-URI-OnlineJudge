#Ler o valor do maior numero representado pelo computador
maiorvalor = int(input())
#ler calculo (valor(P) operação(C) valor(Q)) e tranformar em variaveis
calculo = input().split()
p = int(calculo[0])
c = calculo[1]
q = int(calculo[2])
#se C for igual a '+' faça: some P+Q
#se C for igual a '*' faça: multiplique P*Q
if c == '+':
    operacao = p + q
if c == '*':
    operacao = p * q
#verificar se o calculo foi menor ou igual ao maior valor representado
#dizer se ultepassou 'OVERFLOW', ou nao 'OK'
if operacao <= maiorvalor:
    print('OK')
else:
    print('OVERFLOW')



