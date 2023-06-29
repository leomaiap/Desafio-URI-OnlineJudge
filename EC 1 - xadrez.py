#ler numero de linhas
#ler numero de colunas
linhas = int(input())
colunas = int(input())
L = linhas % 2
C = colunas % 2
#analisando o tabuleiro cheguei a conclusao de:
#se L e C forem iguais = branco 1
#se L(par) e C(par) = branco 1 
#se L(impar) e C(impar) = branco 1
#se L(par) e C(impar) = preto 0
#se L(impar) e C(par) = preto 0
if L == C:
    print(1)
elif L != C:
    print(0)
