# ler 4 horarios
horarios = str(input())
#           1         2
# 01234567890123456789012 indice
# 00:00 00:00 00:00 00:00
# passar horas para minutos
h1, h2 = int(horarios[0:2])*60 + int(horarios[3:5]), int(horarios[6:8])*60 + int(horarios[9:11])
h3, h4 = int(horarios[12:14])*60 + int(horarios[15:17]), int(horarios[18:20])*60 + int(horarios[21:23])

# verificar se a duracao esta no mesmo dia ou no dia seguinte
# se tiver no dia seguinte 24h - (saida + chegada)
# se tiver no mesmo dia (chegada - saida)
#ida
if h1 > h2:
    duracaoida = (24*60) - (h1 + h2)
else:
    duracaoida = h2 - h1
    
#volta
if h3 > h4:
    duracaovolta = (24*60) - (h3+h4)
else:
    duracaovolta = h3 - h4

#calcular duracao do voo
#(media de tempo do voo) e se ultrapassou 1 dia subtrair 12h
if duracaoida + duracaovolta > 24*60:
    duracaovoo = (duracaoida + duracaovolta)/2 - (12*60)
else:
    duracaovoo = (duracaoida + duracaovolta)/2

#calcular diferencade fuso horario
if duracaoida - duracaovoo > 12*60:
    fuso = (duracaoida - duracaovoo - (24*60)) / 60
else:
    fuso = (duracaoida - duracaovoo) / 60

print(f'{duracaovoo} {fuso}')
