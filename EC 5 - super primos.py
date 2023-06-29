primos1dig = ['2','3','5','7']

while True:
    try:
        linha = input()
        Super = 0
        for d in range(len(linha)):
            if linha[d] in primos1dig:
                Super += 1
        
        num = int(linha[:])
        divisoes = 0
        for n in range(1, num+1):
            if num % n == 0:
                divisoes += 1
        
        if divisoes == 2 and Super == len(linha):
            print('Super')
        elif divisoes == 2:
            print('Primo')
        else:
            print('Nada')
    
    except EOFError:
        break
