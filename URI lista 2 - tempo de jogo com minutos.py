tempo = input().split()
hi, mi, hf, mf = int(tempo[0]), int(tempo[1]), int(tempo[2]), int(tempo[3])
h = (hf-hi)
m = (mf-mi)
#print(h, m)

if h < 0:
    h += 24
#print(h)
if m < 0:
    m += 60
    h -= 1
#print(m, h)
if h < 0:
    h += 24
#print(h)

if m == 0 and h == 0:
    print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')
else:
    print('O JOGO DUROU {0} HORA(S) E {1} MINUTO(S)'.format(h, m))
