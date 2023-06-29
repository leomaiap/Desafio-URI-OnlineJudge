#ler dados de fracoes em linha única
#passar para variaveis [0]=numerador1, [1]=denominador1, [2]=numerador2, [3]=denominador2
fracoes = input().split()
num1, den1, num2, den2 = int(fracoes[0]), int(fracoes[1]), int(fracoes[2]), int(fracoes[3])
#verificar denominadores se são iguais ou diferentes e calcular
#se denominadores forem diferentes: faça
if den1 != den2:
    #multiplicar cruzado e somar os resultados, por no numerador
    #e multiplicar denominadores, por no denominador
    numerador = (num1*den2) + (num2*den1)
    denominador = (den1*den2)
#se denominadores forem iguais: faça
elif den1 == den2:
    #soma os numeradores, por no numerador
    #repetir o denominador, por no denominador
    numerador = num1 + num2
    denominador = den1
#Simplificar resultados
#fazer MDC do numerador e denominador(Escolhi o metodo de Euclides para achar o MDC, pois achei o mais fácil de fazer no python)
#depois dividir numerador e denominador pelo MDC

#Algoritimo de Euclides
#divide os 2 ultimos divisores, pega o resto poe em uma lista
#se o resto for 0, o ultimo divisor sera o MDC
#senao: pega o ultimo resto poe na lista de divisores
#repete-se até resto for 0
parar = False
ordenar = [numerador, denominador]
ordenar.sort(reverse=True) #ordena numerador e denominador pra dividir o maior pelo menor
divisores = [ordenar[0], ordenar[1]] #lista de divisores, onde o ultimo sera o MDC quando resto for 0
restoMDC = [] #lista de restos
#repeticao
while parar == False:
    calc = divisores[-2] % divisores[-1] #resto da divisao entre os dois ultimos divisores
    restoMDC.append(calc) #"guardar" restos na memoria
    if calc == 0: #se resto deu 0
        parar = True #Parar fica verdadeiro
        mdc = divisores[-1]  #ultimo da lista divisores sera o MDC
    else: #se resto nao for 0:
        divisores.append(int(restoMDC[-1])) #ultimo resto diferente de 0 vai para final da lista divisores
    #repete
#dividir numerador e denominador pelo mdc 
numerador = numerador/mdc
denominador = denominador/mdc 

#imprimir resultado
print(f'{int(numerador)} {int(denominador)}')
