#ler coordenadas iniciais do retangulo e finais do retangulo 1
ret1 = input().split()
Xi1, Yi1, Xf1, Yf1 = int(ret1[0]), int(ret1[1]), int(ret1[2]), int(ret1[3])
#ler coordenadas iniciais do retangulo e finais do retangulo 2
ret2 = input().split()
Xi2, Yi2, Xf2, Yf2 = int(ret2[0]), int(ret2[1]), int(ret2[2]), int(ret2[3])

L1 = abs(Xi1-Xf1) #largura retangulo 1
A1 = abs(Yi1-Yf1) #altura retangulo 1
L2 = abs(Xi2-Xf2) #largura retangulo 2
A2 = abs(Yi2-Yf2) #altura retangulo 2

colisao = False #Registrar se houve Colisao

#verificar, por exemplo, se X+largura e Y+altura inical 2 esta entre  X iicial 1 e X final 1 | Y iicial 1 e Y final 1
#para haver colisao ColX e ColY ambos tem que ser verdadeiros
if Xi1 <= Xi2 + L2 and Xi1 + L1 >= Xi2 and Yi1 <= Yi2 + A2 and Yi1 + A1 >= Yi2:
	colisao = True

#imprimir resultado
if colisao:
	print('1')
else:
	print('0')

	# 5 5 8 20
	#15 17 18 21




