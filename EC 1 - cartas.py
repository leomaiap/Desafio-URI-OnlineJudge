#ler valores das 5 cartas, colocar em lista
valor = input().split()
lista = []
for v in range(0,5):
    lista.append(int(valor[v]))
#verificar em qual ordem estão as cartas
#crescente
if lista[0] < lista[1] < lista[2] < lista[3] < lista[4]:
    print('C')
#decrescente
elif lista[4] < lista[3] < lista[2] < lista[1] < lista[0]:
    print('D')
#nenhum
else:
    print('N')
