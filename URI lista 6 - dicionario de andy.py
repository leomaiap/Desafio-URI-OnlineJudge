dicionario = []
while True:
    try:
        frase = input().lower()
        for c in frase:
            if not c.isalpha():
                frase = frase.replace(f'{c}', ' ')

        frase = frase.split()

        for f in frase:
            if f not in dicionario:
                dicionario.append(f)

    except EOFError:

        for i in range(len(dicionario)):
            j = i+1
            menor = i
            while j < len(dicionario):
                if dicionario[j] < dicionario[menor]:
                    menor = j
                j += 1
            dicionario[i], dicionario[menor] = dicionario[menor], dicionario[i]
        for p in dicionario:
            print(p)

        break
