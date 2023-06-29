n = int(input())
original = []
metade1 = []
metade2 = []
for i in range(n):
    original.append(i+1)

for m in range(n//2):
    metade1.append(original[m])
    metade2.append(original[m+(n//2)])


contador = 1
while True:
    baralho = []
    for i in range(n//2):
        baralho.append(metade2[i])
        baralho.append(metade1[i])
    
    if baralho == original:
        break
    else:
        metade1 = []
        metade2 = []
        for m in range(n//2):
            metade1.append(baralho[m])
            metade2.append(baralho[m+(n//2)])
        contador += 1

print(contador)