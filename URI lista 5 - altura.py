#ler quanrtidade de testes
teste = int(input())
#ler quantidade de altura a serem digitadas
for x in range(teste):
    quant = int(input())
    alturas = input().split()
    # se item da altura for igual ao x imprime, assim sera colocado em ordenacao
    for x in range(20,231):
        for a in alturas:
            if a == f'{x}':
                print(f'{a}', end=(' '))
               
    print ()
    alturas = []