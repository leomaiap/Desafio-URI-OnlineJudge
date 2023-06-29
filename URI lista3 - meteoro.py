parar = False
numteste = 1
cairam = 0
Xatingido = False
Yatingido = False
while not parar:
    fazenda = input().split()
    x1, y1, x2, y2 = int(fazenda[0]), int(fazenda[1]), int(fazenda[2]), int(fazenda[3])
    if x1 == 0 and x2 == 0 and y1 == 0 and y2 == 0:
        break
    meteoritos = int(input())
    for c in range(meteoritos):
        coordnadaqueda = input().split()
        qx, qy = int(coordnadaqueda[0]), int(coordnadaqueda[1])
        if x1 <= qx <= x2:
            Xatingido = True
        if y2 <= qy <= y1:
            Yatingido = True
        if Xatingido == True and Yatingido == True:
            cairam += 1
        Xatingido = False
        Yatingido = False

    print('Teste {}'.format(numteste))
    print(cairam)
    cairam = 0
    numteste += 1
    