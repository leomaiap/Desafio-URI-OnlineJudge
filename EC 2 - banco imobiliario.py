#ler primeira linha separar em 2 variaveis (dinheiro inicial e numero de operações)
dados = input().split()
dinheiroInicial = int(dados[0])
operacoes = int(dados[1])
#jogadores recebem valor de dinheiro inicial
dalia = dinheiroInicial
eloi = dinheiroInicial
felix = dinheiroInicial
#repetir N vez operação
for o in range(operacoes):
    #ler tipo de operacao, jogador, valor gasto (ou recebido)
    #colocar em variaveis #operacoes (c - compra) (v - venda) (a - aluguel)    
    op = input().split()
    #se for aluguel faça (ler 2 jogadores  jogador pagador e jogador recebedor, e dinheiro)
    if op[0] == 'A':
        tipo = op[0]
        jogA = op[1]
        jogB = op[2]
        dinheiro = int(op[3])
    #senao leia 1 jogador apenas e dinheiro
    else:
        tipo = op[0]
        jogA = op[1]
        dinheiro = int(op[2])

    '''
    se tipo for 'A' faça:
        identificar jogA e jogB
            jogA perde dinheiro
            jogB recebe dinheiro'''
    if tipo == 'A':
        if jogA == 'D':
            dalia += dinheiro
        elif jogA == 'E':
            eloi += dinheiro
        elif jogA == 'F':
            felix += dinheiro
        
        if jogB == 'D':
            dalia -= dinheiro
        elif jogB == 'E':
            eloi -= dinheiro
        elif jogB == 'F':
            felix -= dinheiro
    '''
    se tipo for 'C' faça:
        identificar jogA
            jogA perde dinheiro'''
    if tipo == 'C':
        if jogA == 'D':
            dalia -= dinheiro
        elif jogA == 'E':
            eloi -= dinheiro
        elif jogA == 'F':
            felix -= dinheiro
    '''
    se tipo for 'V' faça:
        identificar jogA
            jogA recebe dinheiro'''
    if tipo == 'V':
        if jogA == 'D':
            dalia += dinheiro
        elif jogA == 'E':
            eloi += dinheiro
        elif jogA == 'F':
            felix += dinheiro

#mostrar resultados do saldo de cada jogador
print(f'{dalia} {eloi} {felix}')





