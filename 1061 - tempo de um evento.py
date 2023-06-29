d = input().split()
h = input().split(' : ')
diaIni = int(d[1])
horaIni = int(h[0])
minIni = int(h[1])
segIni = int(h[2])
df = input().split()
hf = input().split(' : ')
diaF = int(df[1])
horaF = int(hf[0])
minF = int(hf[1])
segF = int(hf[2])

dia = diaF-diaIni
hora = horaF-horaIni
minuto = minF-minIni
segundo = segF-segIni

if segundo < 0:
    segundo += 60
    minuto -= 1

if minuto < 0:
    minuto += 60
    hora -= 1

if hora < 0:
    hora += 24
    dia -= 1

print(f'{dia} dia(s)')
print(f'{hora} hora(s)')
print(f'{minuto} minuto(s)')
print(f'{segundo} segundo(s)')
