quantmatriz = int(input())
for gerar in range(quantmatriz):
    sudoku = []
    for linhavazia in range(9):
        sudoku.append([])
    for l in range(9):
        linha = input().split()
        for c in range(9):
            sudoku[l].append(int(linha[c]))
    #print(sudoku)
    linha0 = []
    linha1 = [] 
    linha2 = [] 
    linha3 = [] 
    linha4 = []
    linha5 = []
    linha6 = []
    linha7 = []
    linha8 = []

    col0 = []
    col1 = [] 
    col2 = [] 
    col3 = [] 
    col4 = []
    col5 = []
    col6 = []
    col7 = []
    col8 = []
    
    bloco0 = []
    bloco1 = []
    bloco2 = []
    bloco3 = []
    bloco4 = []
    bloco5 = []
    bloco6 = []
    bloco7 = []
    bloco8 = []
    #LINHAS
    for l in range(0,9):
        for c in range(0,9):
            if l == 0:
                if sudoku[l][c] not in linha0:
                    linha0.append(sudoku[l][c])
            if l == 1:
                if sudoku[l][c] not in linha1:
                    linha1.append(sudoku[l][c])
            if l == 2:
                if sudoku[l][c] not in linha2:
                    linha2.append(sudoku[l][c])
            if l == 3:
                if sudoku[l][c] not in linha3:
                    linha3.append(sudoku[l][c])
            if l == 4:
                if sudoku[l][c] not in linha4:
                    linha4.append(sudoku[l][c])
            if l == 5:
                if sudoku[l][c] not in linha5:
                    linha5.append(sudoku[l][c])
            if l == 6:
                if sudoku[l][c] not in linha6:
                    linha6.append(sudoku[l][c])
            if l == 7:
                if sudoku[l][c] not in linha7:
                    linha7.append(sudoku[l][c])
            if l == 8:
                if sudoku[l][c] not in linha8:
                    linha8.append(sudoku[l][c])
    #COLUNAS
    for c in range(0,9):
        for l in range(0,9):
            if c == 0:
                if sudoku[l][c] not in col0:
                    col0.append(sudoku[l][c])
            if c == 1:
                if sudoku[l][c] not in col1:
                    col1.append(sudoku[l][c])
            if c == 2:
                if sudoku[l][c] not in col2:
                    col2.append(sudoku[l][c])
            if c == 3:
                if sudoku[l][c] not in col3:
                    col3.append(sudoku[l][c])
            if c == 4:
                if sudoku[l][c] not in col4:
                    col4.append(sudoku[l][c])
            if c == 5:
                if sudoku[l][c] not in col5:
                    col5.append(sudoku[l][c])
            if c == 6:
                if sudoku[l][c] not in col6:
                    col6.append(sudoku[l][c])
            if c == 7:
                if sudoku[l][c] not in col7:
                    col7.append(sudoku[l][c])
            if c == 8:
                if sudoku[l][c] not in col8:
                    col8.append(sudoku[l][c])

    #bloco0    
    for l in range(0,3):
        for c in range(0,3):
            if sudoku[l][c] not in bloco0:
                bloco0.append(sudoku[l][c])
    #bloco1    
    for l in range(0,3):
        for c in range(3,6):
            if sudoku[l][c] not in bloco1:
                bloco1.append(sudoku[l][c])
    #bloco2    
    for l in range(0,3):
        for c in range(6,9):
            if sudoku[l][c] not in bloco2:
                bloco2.append(sudoku[l][c])

    for l in range(3,6):
        for c in range(0,3):
            if sudoku[l][c] not in bloco3:
                bloco3.append(sudoku[l][c])
    
    for l in range(3,6):
        for c in range(3,6):
            if sudoku[l][c] not in bloco4:
                bloco4.append(sudoku[l][c])
        
    for l in range(3,6):
        for c in range(6,9):
            if sudoku[l][c] not in bloco5:
                bloco5.append(sudoku[l][c])   
    
    for l in range(6,9):
        for c in range(0,3):
            if sudoku[l][c] not in bloco6:
                bloco6.append(sudoku[l][c])
    
    for l in range(6,9):
        for c in range(3,6):
            if sudoku[l][c] not in bloco7:
                bloco7.append(sudoku[l][c])
    #bloco8
    for l in range(6,9):
        for c in range(6,9):
            if sudoku[l][c] not in bloco8:
                bloco8.append(sudoku[l][c])
    print(f'Instancia {gerar+1}')
    if len(bloco0) == len(bloco1) == len(bloco2) == len(bloco3) == len(bloco4) == len(bloco5) == len(bloco6) == len(bloco7) == len(bloco8) == len(linha0) == len(linha1) == len(linha2) == len(linha3) == len(linha4) == len(linha5) == len(linha6) == len(linha7) == len(linha8) == len(col0) == len(col1) == len(col2) == len(col3) == len(col4) == len(col5) == len(col6) == len(col7) == len(col8) == 9:
        print('SIM')
    else:
        print('NAO')
