#ler quantidade de entradas (N)
n = int(input())

finalA = [] #salvar temporariamente os ultinos N caracteres de A (len(B))

for q in range(n):
    ab = input().split()
    a, b = ab[0], ab[1]
    
    if len(a)<len(b):
        finalA.append(a[-len(b):]) #salva os -Len de b ultimos caracteres

        if finalA[0] == b: # se finalfor igual a B entao encaixa:
            print("encaixa")
        else:
            print("nao encaixa")
    else:
         print("nao encaixa")











