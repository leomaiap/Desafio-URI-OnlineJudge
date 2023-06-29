chave = input()
quantfrase = int(input())
for q in range(quantfrase):
    frase = input().split()
    for f in range(len(frase)):
        chavefrase = 0
        if frase[f][0] not in 'aeiou':
            print('#####', end=' ')    

        else:
            print(frase[f], end=' ')
    print()