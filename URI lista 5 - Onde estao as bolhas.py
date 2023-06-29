# ler n e m (n =  ate onde vai a lista, m = numero de rodadas)
# enquanto nm != 0 faca
nm = input().split()
while nm != '0 0':
    n, m = int(nm[0]), int(nm[1])
    rodadas = []
    rod = input().split()
    for r in range(m):
        rodadas.append(int(rod[r]))

    seq = []
    for s in range(n, 0, -1):
        seq.append(s)

    for i in range(n):
        for j in range(n-1, i, -1):
            if seq[j-1] > seq[j]:
                seq[j], seq[j-1] = seq[j-1], seq[j]
               


    print(seq)
