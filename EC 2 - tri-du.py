#ler valor de duas cartas
cartas = input().split()
a = int(cartas[0])
b = int(cartas[1])
# dizer o melhor resultado para vencer
#se as 2 cartas forem iguais a 3ª sera de mesmo valor das 2 cartas
#se 2 cartas forem diferentes a 3ª carta será de mesmo valor da maior carta
if a == b:
    print(a)
elif a < b:
    print(b)
elif a > b:
    print(a)
