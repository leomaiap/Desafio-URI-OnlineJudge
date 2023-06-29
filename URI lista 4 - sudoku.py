quantmatriz = int(input())
errado = False
for gerar in range(quantmatriz):
    sudoku = []
    for linhavazia in range(9):
        sudoku.append([])
    for l in range(9):
        linha = input().split()
        for c in range(9):
            sudoku[l].append(int(linha[c]))
    #print(sudoku)
    linhas1 = [] #L 0 até 2
    linhas2 = [] #L 3 até 5
    linhas3 = [] #L 6 ate 8

    for l in range(0,9,3):#L 0, 3, 6
        for ll in range(l, l+3):#L(0,1,3) (4,5,6) (7,8,9)
            for c in range(0,9,3):#C 0, 3, 6
                for cc in range(c, c+3):#C(0,1,3) (4,5,6) (7,8,9)
                    if c == 0:
                        if sudoku[ll][cc] not in linhas1:
                            linhas1.append(sudoku[ll][cc])
                    if c == 3:
                        if sudoku[ll][cc] not in linhas2:
                            linhas2.append(sudoku[ll][cc])
                    if c == 6:
                        if sudoku[ll][cc] not in linhas3:
                            linhas3.append(sudoku[ll][cc])
        #print(linhas1)
        #print(linhas2)
        #print(linhas3)
        if len(linhas1) != 9:
            errado = True
        if len(linhas2) != 9:
            errado = True
        if len(linhas3) != 9:
            errado = True
        linhas1 = []
        linhas2 = []
        linhas3 = []
    print(f'Instancia {gerar+1}')
    if errado:
        print('NAO')
    else:
        print('SIM')
    print()
    errado = False

