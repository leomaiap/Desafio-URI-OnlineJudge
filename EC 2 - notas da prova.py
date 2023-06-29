#ler valor da nota em numero inteiro
nota = int(input())
#converter nota de decimal para conceito
# (86 a 100 = A), (61 a 85 = B), (36 a 60 = C), (1 a 35 = D) (0 = E)
if nota == 0:
    print('E')
if 1 <= nota <= 35:
    print('D')
if 36 <= nota <= 60:
    print('C')
if 61 <= nota <= 85:
    print('B')
if 86 <= nota <= 100:
    print('A')
