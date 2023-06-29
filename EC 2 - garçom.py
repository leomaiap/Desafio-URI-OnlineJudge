#ler quantidade de bandejas (será o numero de linhas digitadas)
bandejas = int(input())
quebrados = 0 #copos que se quebraram
#ler quantidades de latas e copos de cada N bandeja, colocar em variaveis
for b in range(bandejas):
    itens = input().split()
    lata = int(itens[0])
    copo = int(itens[1])
    #se o numero de copos for menor que a quantidades de latas, quevrar recebe numero de copos
    #senao nada fazer
    if copo < lata:
        quebrados += copo
#resultado de quantos copos quebraram
print(quebrados)