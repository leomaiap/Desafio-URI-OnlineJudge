#ler N(quantidade de pinos), M(altura correta dos pinos)
nm = input().split()
n, m = int(nm[0]), int(nm[1])
#ler alturas dos pinos, linha unica
pinos = input().split()
alturas = []
for p in pinos:
    alturas.append(int(p))
#contar movimentos
#fazer diferenca entre altura do pino[i] e alturacorreta do pino
#adicionar o valor absoluto ao proximo item da lista [i+1]
#adicionar o valor da diferenca a um contador de movimentos
movimentos = 0
for i in range(len(alturas)-1):
    alteracaoaltura = abs(alturas[i]-m)
    alturas[i+1] += alteracaoaltura
    movimentos += alteracaoaltura
print(movimentos)
