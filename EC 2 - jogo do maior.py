#ler numero de rodadas, 0 interrompe
#rodadas = int(input())
while True:
    rodadas = int(input())
    if rodadas == 0:
        break
    jog1 = 0
    jog2 = 0 #placar dos jogadores
    #ler valores de cada rodada, e comparar, e quem ganhar soma 1 ponto em caso de empate 0
    for r in range(rodadas):
        num = input().split()
        if int(num[0]) > 10:
            jog2 += 1
        elif int(num[1]) > 10:
            jog1 += 1
        elif int(num[0]) > int(num[1]): #se A > B jogador 1 soma 1 ponto 
            jog1 += 1
        elif int(num[0]) < int(num[1]): #se A < B jogador 2 soma 1 ponto 
            jog2 += 1
        
    #resultados
    print(jog1, jog2)
    
