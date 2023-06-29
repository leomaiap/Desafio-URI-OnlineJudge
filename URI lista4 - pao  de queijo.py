while True:
    try:
        nm = input().split()
        nL = int(nm[0])
        nC = int(nm[1])
        matriz = []
        for vazia in range(nL):
            matriz.append([])
        for l in range(nL):
            linha = input().split()
            for c in range(nC):
                matriz[l].append(int(linha[c]))
        #print(matriz)
        '''-
        ↑ - L -1  if matriz[l-1][c] == 1:contador += 1
        ↓ - L +1  if matriz[l+1][c] == 1:contador += 1
        → - C +1  if matriz[l][c+1] == 1:contador += 1
        ← - C -1  if matriz[l][c-1] == 1:contador += 1
               
        primeira linha
        SE linha == 0 and coluna == 0: verificar ↓ →
        SE linha == 0 and 0 < coluna <= (nC -2): verificar ← ↓ →
        SE linha == 0 and coluna == (nC -1): verificar ← ↓
        
        meio linha
        SE 0 < linha <= (nL -2) and coluna == 0: verificar ↑ ↓ →
        SE 0 < linha <= (nL -2) and 0 < coluna <= nC -2: verificar ← ↑ ↓ →
        SE 0 < linha <= (nL -2) and coluna == (nC -1): verificar ← ↑ ↓
        
        última linha
        SE linha == (nL -1) and coluna == 0: verificar ↑ →
        SE linha == (nL -1) and and 0 < coluna <= nC -2: verificar ← ↑ →
        SE linha == (nL -1) and and coluna == (nC -1): verificar ← ↑ 
        
            SE matriz[l][c] == 1:
                analise append 9
            contador = 0
            SEnao SE ↑ ↓ → ← == 0:
                contador += 1 (para cada seta)
            analise append contador       
        '''
        analise = []
        if nL == 1 and nC > 1:
            l = 0
            for c in range(nC+1):                    
                if l == 0 and c == 0:
                        if matriz[l][c] == 1:
                            analise.append(9)
                        else:
                            contador = 0
                            if matriz[l][c+1] == 1:
                                contador += 1
                            analise.append(contador)
                if nC > 2:
                    if l == 0 and 0 < c <= (nC-2):
                            if matriz[l][c] == 1:
                                analise.append(9)
                            else:
                                contador = 0
                                if matriz[l][c-1] == 1:
                                    contador += 1
                                if matriz[l][c+1] == 1:
                                    contador += 1
                                analise.append(contador)
                if l == 0 and c == (nC-1):
                        if matriz[l][c] == 1:
                            analise.append(9)
                        else:
                            contador = 0
                            if matriz[l][c-1] == 1:
                                contador += 1
                            analise.append(contador)
                #print(analise)        
                #analise = []        
        
        if nL > 1 and nC == 1:
            c = 0
            for l in range(nL+1):
                if l == 0 and c == 0:
                        if matriz[l][c] == 1:
                            analise.append(9)
                        else:
                            contador = 0
                            if matriz[l+1][c] == 1:
                                contador += 1
                            analise.append(contador)
                if nL > 2:
                    if 0 < l <= (nL-2) and c ==0:
                            if matriz[l][c] == 1:
                                analise.append(9)
                            else:
                                contador = 0
                                if matriz[l-1][c] == 1:
                                    contador += 1
                                if matriz[l+1][c] == 1:
                                    contador += 1
                                analise.append(contador)
                if l == (nL-1) and c == 0:
                        if matriz[l][c] == 1:
                            analise.append(9)
                        else:
                            contador = 0
                            if matriz[l-1][c] == 1:
                                contador += 1
                            analise.append(contador)
                #print(analise)        
                #analise = []
        
        if nL == 1 and nC == 1:
            if matriz[0][0] == 1:
                analise.append(9)
            else:
                analise.append(0)
            #print(analise)        
            
        
        if nL > 1 and nC > 1:
            for l in range(0, nL+1):
                for c in range(0, nC+1):
                    #primera linha
                    if l == 0 and c == 0:
                        if matriz[l][c] == 1:
                            analise.append(9)
                        else:
                            contador = 0
                            if matriz[l+1][c] == 1:
                                contador += 1
                            if matriz[l][c+1] == 1:
                                contador += 1
                            analise.append(contador)
                    if l == 0 and 0 < c <= (nC-2):
                        if matriz[l][c] == 1:
                            analise.append(9)
                        else:
                            contador = 0
                            if matriz[l][c-1] == 1:
                                contador += 1
                            if matriz[l+1][c] == 1:
                                contador += 1
                            if matriz[l][c+1] == 1:
                                contador += 1
                            analise.append(contador)
                    if l == 0 and c == (nC-1):
                        if matriz[l][c] == 1:
                            analise.append(9)
                        else:
                            contador = 0
                            if matriz[l][c-1] == 1:
                                contador += 1
                            if matriz[l+1][c] == 1:
                                contador += 1
                            analise.append(contador)
                    #linhas meio (se houver)
                    if 0 < l <= (nL-2) and c ==0:
                        if matriz[l][c] == 1:
                            analise.append(9)
                        else:
                            contador = 0
                            if matriz[l-1][c] == 1:
                                contador += 1
                            if matriz[l+1][c] == 1:
                                contador += 1
                            if matriz[l][c+1] == 1:
                                contador += 1
                            analise.append(contador)
                    if 0 < l <= (nL-2) and 0 < c <= (nC-2):
                        if matriz[l][c] == 1:
                            analise.append(9)
                        else:
                            contador = 0
                            if matriz[l-1][c] == 1:
                                contador += 1
                            if matriz[l+1][c] == 1:
                                contador += 1
                            if matriz[l][c+1] == 1:
                                contador += 1
                            if matriz[l][c-1] == 1:
                                contador += 1
                            analise.append(contador)
                    if 0 < l <= (nL-2) and c == (nC-1):
                        if matriz[l][c] == 1:
                            analise.append(9)
                        else:
                            contador = 0
                            if matriz[l-1][c] == 1:
                                contador += 1
                            if matriz[l+1][c] == 1:
                                contador += 1
                            if matriz[l][c-1] == 1:
                                contador += 1
                            analise.append(contador)
                    #ultima linha
                    if l == (nL-1) and c == 0:
                        if matriz[l][c] == 1:
                            analise.append(9)
                        else:
                            contador = 0
                            if matriz[l-1][c] == 1:
                                contador += 1
                            if matriz[l][c+1] == 1:
                                contador += 1
                            analise.append(contador)
                    if l == (nL-1) and 0 < c <= (nC-2):
                        if matriz[l][c] == 1:
                            analise.append(9)
                        else:
                            contador = 0
                            if matriz[l][c-1] == 1:
                                contador += 1
                            if matriz[l-1][c] == 1:
                                contador += 1
                            if matriz[l][c+1] == 1:
                                contador += 1
                            analise.append(contador)
                    if l == (nL-1) and c == (nC-1):
                        if matriz[l][c] == 1:
                            analise.append(9)
                        else:
                            contador = 0
                            if matriz[l][c-1] == 1:
                                contador += 1
                            if matriz[l-1][c] == 1:
                                contador += 1
                            analise.append(contador)
                    
        for i in range(0, len(analise), nC):
            for ii in range(i, i+nC):
                if ii == 0:
                    print(f'{analise[ii]}', end=(''))
                elif i == ii:
                    print(f'\n{analise[ii]}', end=(''))
                elif ii != 0:
                    print(f'{analise[ii]}', end=(''))
        print()
        #print(analise)
    except EOFError:
        break


