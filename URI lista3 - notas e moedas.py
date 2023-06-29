valor = float(input())

real = valor // 1
cent = valor - real
centavos = round(cent, 2) * 100

ced100, ced50, ced20, ced10, ced5, ced2, = 0, 0, 0, 0, 0, 0
m100, m50, m25, m10, m5, m1 = 0, 0, 0, 0, 0, 0

while real > 0:
    if 100 <= real <= 10000000:
        ced100 = real // 100
        real -= (ced100 * 100)
    elif 50 <= real < 100:
        ced50 = real // 50
        real -= (ced50 * 50)
    elif 20 <= real < 50:
        ced20 = real // 20
        real -= (ced20 * 20)
    elif 10 <= real < 20:
        ced10 = real // 10
        real -= (ced10 * 10)
    elif 5 <= real < 10:
        ced5 = real // 5
        real -= (ced5 * 5)
    elif 2 <= real < 5:
        ced2 = real // 2
        real -= (ced2 * 2)
    elif 1 <= real < 2:
        m100 = 1
        real -= 1
#moedas ↓   ↓   ↓ 
while centavos > 0:    
    if 50 <= centavos < 100:
        m50 = 1
        centavos -= 50
    elif 25 <= centavos < 50:
        m25 = 1
        centavos -= 25
    elif 10 <= centavos < 25:
        m10 = centavos // 10
        centavos -= m10 * 10
    elif 5 <= centavos < 10:
        m5 = 1
        centavos -= 5
    elif 1 <= centavos <  5:
        m1 = centavos // 1
        centavos -= m1 * 1
    
       
print('NOTAS:')
print('{} nota(s) de R$ 100.00'.format(int(ced100)))
print('{} nota(s) de R$ 50.00'.format(int(ced50)))
print('{} nota(s) de R$ 20.00'.format(int(ced20)))
print('{} nota(s) de R$ 10.00'.format(int(ced10)))
print('{} nota(s) de R$ 5.00'.format(int(ced5)))
print('{} nota(s) de R$ 2.00'.format(int(ced2)))
print('MOEDAS:')
print('{} moeda(s) de R$ 1.00'.format(int(m100)))
print('{} moeda(s) de R$ 0.50'.format(int(m50)))
print('{} moeda(s) de R$ 0.25'.format(int(m25)))
print('{} moeda(s) de R$ 0.10'.format(int(m10)))
print('{} moeda(s) de R$ 0.05'.format(int(m5)))
print('{} moeda(s) de R$ 0.01'.format(int(m1)))
