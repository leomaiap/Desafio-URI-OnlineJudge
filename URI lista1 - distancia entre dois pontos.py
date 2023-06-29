p1 = input('').split()
p2 = input('').split()
x1, y1, x2, y2 = float(p1[0]), float(p1[1]), float(p2[0]), float(p2[1])
calculo = (((x2-x1)**2)+((y2-y1)**2))**(1/2)      
print('{:.4f}'.format(calculo))




'''

posAtk_Y = 100
posAtk_Y = 100

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
            distancia = (((posAtk_Y-areaXinimigo[ax])**2)+((posAtk_Y-areaYinimigo[ay])**2))**(1/2)
            print(distancia)'''