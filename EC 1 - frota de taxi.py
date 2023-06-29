#ler entrada float e criar uma variavel para cada item
dados = input().split()
a, g, kma, kmg = float(dados[0]), float(dados[1]), float(dados[2]), float(dados[3])
#calcular preço por kilometro, o menor sera o escolhido (combustivel/kilometros)
#se ambos forem iguais gasolina sera ecolhida
precoKMa = (a) / (kma)
precoKMg = (g) / (kmg)
#print(precoKMa)
#print(precoKMg)
if precoKMa == precoKMg:
    print('G')
elif precoKMa < precoKMg:
    print('A')
else:
    print('G')
