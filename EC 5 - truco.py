partidas = int(input())
#ordem 4 5 6 7 (Q=12) (J=11) (K=13) (A=1) 2 3
totalA, totalB = 0, 0
for p in range(partidas):
    pontosA, pontosB = 0, 0
    cartas = list(map(int, input().split()))
    for c in range(3):
        if cartas[c] == 12:
            cartas[c] = 9
        if cartas[c] in [1, 2, 3]:
            cartas[c] += 15
        
        if cartas[c+3] == 12:
            cartas[c+3] = 9
        if cartas[c+3] in [1, 2, 3]:
            cartas[c+3] += 15

        if cartas[c] >= cartas[c+3]:
            pontosA += 1
        else:
            pontosB += 1
    
    if pontosA > pontosB:
        totalA += 1
    else:
        totalB += 1
print(totalA, totalB)