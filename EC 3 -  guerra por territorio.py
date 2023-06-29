#ler tamanho da seção do territorio
n = int(input())
lista = []
#Ler N valores em linha unica, colocar em lista
valor = input().split()
for v in range(n):
    lista.append(int(valor[v]))
#somar lista, e achar o valor da metade
valor = []
soma = 0
for s in lista:
    soma += s
metade = soma//2
#achar o valor de K de qual seção K sera dividido
# K sera  igual ao i+1 de onde a soma for = metade
#enquanto a soma nao for = a metade faça a soma
soma2 = 0
indice = 0
for s2 in lista:
    soma2 += s2
    indice += 1
    if soma2 == metade:
        break
#imprimir resultado indice
print(indice)