nm = input().split()
numLinha = int(nm[0])
numColuna = int(nm[1])
matriz = []
#gerador de matriz vazia
for linhavazia in range(numLinha):
    matriz.append([])

#print(matriz)

for l in range(numLinha):
    linha = input().split()
    for c in range(numColuna):
        matriz[l].append((linha[c]))

'''
[L-1 C-1]   [ L-1 ]   [L-1 C+1]

[  C-1  ]   [LC-42]   [  C+1  ]

[L+1 C-1]   [ L+1 ]   [L+1 C+1]
'''
encontrado = False
while True:
    for l in range(1, numLinha-1):
        for c in range(1, numColuna-1):
            if matriz[l][c] == '42':
                if matriz[l][c-1] == matriz[l][c+1] == '7':
                    if matriz[l-1][c] == matriz[l+1][c] == '7':
                        if matriz[l-1][c-1] == matriz[l-1][c+1] == '7':
                            if matriz[l+1][c-1] == matriz[l+1][c+1] == '7':
                                print(f'{l+1} {c+1}')
                                encontrado = True
                                break
    
    break
if encontrado == False:
    print('0 0')