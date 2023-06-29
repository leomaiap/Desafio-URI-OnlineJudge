#ler RGB e converter de hexadecimal para decimal
r = int(input(), 16)
g = int(input(), 16)
b = int(input(), 16)
#print(r, g, b)
#azul cabe em verde, verde cabe em vermelho

#vermelho = 1 #quantidade de vermelho

#lado do verde é igual a divisão inteira de r por g
verde = r // g 
verde *= verde # quantidade de verde = lado x lado
#print(verde)
#lado do azul é igual a divisão inteira de g por b
azul = g // b
azul *= azul #quantidade lado x lado
azul *= verde #quantidade achada no passo anterior x quantidade de verdes = quantidade de azul
#print(azul)
etiquetas = 1 + verde + azul #quantidade de etiquetas = soma quantidade de verdes + azuis + vermelho(que existe apenas 1)
#print(etiquetas)
etiquetas = hex(etiquetas)
print(etiquetas[2:])