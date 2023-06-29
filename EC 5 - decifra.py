alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
sequencia = input()#ler chave
chave = []
#fazer um "alfabeto" com essa chave
for l in sequencia:
    chave.append(l)
#ler texto criftografado
texto = input()
#descriptografar o texto
for c in range(len(texto)):
    decif = chave.index(texto[c])
    print(f'{alfabeto[decif]}', end=(''))