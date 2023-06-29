numeros = input().split()
a, b = int(numeros[0]), int(numeros[1])
if b%a == 0 or a%b == 0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')