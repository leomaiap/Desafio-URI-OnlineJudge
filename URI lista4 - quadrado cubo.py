lados = 1
while lados > 0:
    try:
        lados = int(input())
        s2 = 0 #Quadrados 2D
        s3 = 0 #Quadrados 3D
        s4 = 0 #Quadrados 4D
        r2 = 0 #Retangulos 2D
        r3 = 0 #Retangulos 3D
        r4 = 0 #Retangulos 4D

        for l in range(1, lados+1):
            calculo = l**2
            s2 += calculo
            calculo = l**3
            s3 += calculo
            calculo = l**4
            s4 += calculo

        r2 = s3 - s2
        r4 = (s3 * s3) - s4
        formula = ((lados*(lados+1))/2)
        r3 = (int(formula)-1)*s3

        print(s2, r2, s3, r3, s4, r4)
        print(f'formula {formula}')
    except EOFError:
        break