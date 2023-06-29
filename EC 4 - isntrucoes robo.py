quantTestes = int(input())
for q in range(quantTestes):
    numinstrucoes = int(input())
    eixoX = 0
    historicoX = []
    for n in range(numinstrucoes):
        intrucao = input().split()
        if intrucao[0][0] == 'L':
            eixoX += -1
            historicoX.append(-1)
        elif intrucao[0][0] == 'R':
            eixoX += 1
            historicoX.append(1)
        elif intrucao[0][0] == 'S':
            mesmo = int(intrucao[2])
            eixoX += historicoX[mesmo-1]
            historicoX.append(historicoX[mesmo-1])
    print(eixoX)