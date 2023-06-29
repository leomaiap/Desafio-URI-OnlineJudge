# ler 4 horarios
horarios = str(input())
#           1         2
# 01234567890123456789012 indice
# 00:00 00:00 00:00 00:00
# passar horas para minutos
h1, h2 = int(horarios[0:2])*60 + int(horarios[3:5]), int(horarios[6:8])*60 + int(horarios[9:11])
h3, h4 = int(horarios[12:14])*60 + int(horarios[15:17]), int(horarios[18:20])*60 + int(horarios[21:23])
#diferenca ida 
duracaoAB = h2 - h1
#diferenca volta
duracaoBA = h4 - h3

duracao = (duracaoAB + duracaoAB)/2
if duracao < 0:
    duracaoAB += 1440

duracao = (duracaoAB + duracaoAB)/2
fuso = (duracaoAB - duracao)/60

if fuso > 12:
    fuso = fuso -12 + -12
elif fuso < -12:
    fuso = (fuso * -1) -12 + -12

fuso = int(fuso)
duracao = int(duracao)

print(duracao, fuso)
