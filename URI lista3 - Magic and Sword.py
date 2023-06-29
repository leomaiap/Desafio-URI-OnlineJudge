casos = int(input())
tabela = [[200, 20, 30, 50],[300, 10, 25, 40],[400, 25, 55, 70],[100, 18, 38, 60]]
#FIRE 0 - WATER 1 - EARTH 2 - AIR 3 [DANO, LV1, LV2, LV3]
dano = 0

while casos != 0:
    linha2 = input().split()
    largura, altura, x0, y0 = int(linha2[0]), int(linha2[1]), int(linha2[2]), int(linha2[3]) 

    linha3 = input().split()
    magia, lvl, posAtk_X, posAtk_Y = str(linha3[0]), int(linha3[1]), int(linha3[2]), int(linha3[3])

    if magia == 'fire':
        atk = tabela[0][0]
        if lvl == 1:
            raio = tabela[0][1]
        if lvl == 2:
            raio = tabela[0][2]
        if lvl == 3:
            raio = tabela[0][3]           
    if magia == 'water':
        atk = tabela[1][0]
        if lvl == 1:
            raio = tabela[1][1]
        if lvl == 2:
            raio = tabela[1][2]
        if lvl == 3:
            raio = tabela[1][3]
    if magia == 'earth':
        atk = tabela[2][0]
        if lvl == 1:
            raio = tabela[2][1]
        if lvl == 2:
            raio = tabela[2][2]
        if lvl == 3:
            raio = tabela[2][3]
    if magia == 'air':    
        atk = tabela[3][0]
        if lvl == 1:
            raio = tabela[3][1]
        if lvl == 2:
            raio = tabela[3][2]
        if lvl == 3:
            raio = tabela[3][3]
    
    #area do inimigo
    areaXinimigo = []
    areaYinimigo = []
    for xi in range(x0, (x0+largura+1)):
        areaXinimigo.append(xi)
    for yi in range(y0, (y0+altura+1)):
        areaYinimigo.append(yi)

    #testar se algum ponto da area do inimigo esta dentro da areado circulo do ataque
    #formula Raiz quadrada de ((x2-x1)^2)+((y2-y1)^2)
    # x2 → posAtk_X    y2 → posAtk_Y
    pontoatingido = 0
    while pontoatingido == 0:
        for ax in range(len(areaXinimigo)):
            for ay in range(len(areaYinimigo)): 
                distancia = (((posAtk_X-areaXinimigo[ax])**2)+((posAtk_Y-areaYinimigo[ay])**2))**(1/2)
                #print(distancia)
                if distancia <= raio:
                    pontoatingido = 1
                    dano = atk
        break
    print(dano)
    
    dano = 0
    casos -= 1
'''print(areaXinimigo, 'iX')
print(areaXatk, 'aX')
print()
print(areaXinimigo, 'iY')
print(areaYatk, 'aY')'''