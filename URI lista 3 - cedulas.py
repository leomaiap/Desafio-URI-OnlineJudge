#URI 1018
#programa para calcular quantidade minima de cédulas necessárias
#para formar o valor de entrada
valor = int(input())
valorinicial = valor
ced100, ced50, ced20, ced10, ced5, ced2, ced1 = 0, 0, 0, 0, 0, 0, 0
while valor != 0:
    if 100 <= valor <= 1000000:
        ced100 = valor // 100
        valor -= (ced100 * 100)
    elif 50 <= valor <= 99:
        ced50 = valor // 50
        valor -= (ced50 * 50)
    elif 20 <= valor <= 49:
        ced20 = valor // 20
        valor -= (ced20 * 20)
    elif 10 <= valor <= 19:
        ced10 = valor // 10
        valor -= (ced10 * 10)
    elif 5 <= valor <= 9:
        ced5 = valor // 5
        valor -= (ced5 * 5)
    elif 2 <= valor <= 4:
        ced2 = valor // 2
        valor -= (ced2 * 2)
    elif valor == 1:
        ced1 = valor // 1
        valor -= 1
print(valorinicial)
print('{} nota(s) de R$ 100,00'.format(ced100))
print('{} nota(s) de R$ 50,00'.format(ced50))
print('{} nota(s) de R$ 20,00'.format(ced20))
print('{} nota(s) de R$ 10,00'.format(ced10))
print('{} nota(s) de R$ 5,00'.format(ced5))
print('{} nota(s) de R$ 2,00'.format(ced2))
print('{} nota(s) de R$ 1,00'.format(ced1))
#Solution by Leonardo Maia - UFF-RJ BR
