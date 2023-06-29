n = int(input())
while n != 0:
    susp = [None] *n
    posicao = [None] *n
    suspeito = input().split()
    for i in range(n):
        susp[i] = int(suspeito[i])
        posicao[i] = i+1
    for a in range(len(susp)-1):
        b = a + 1
        menor = a
        while b < len(susp): 
            if susp[a] < susp[b]:
                menor = b
            b += 1
        susp[a], susp[menor] = susp[menor], susp[a]
        posicao[a], posicao[menor] = posicao[menor], posicao[a]
    print(posicao[1])
    n = int(input())