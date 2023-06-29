#ler coordenada de Maria(X,Y) e coordenada da reunião(X,Y), separa-las em variaveis
coord =  input().split()
Xm, Ym, Xr, Yr = int(coord[0]), int(coord[1]), int(coord[2]), int(coord[3])
#contar em quantos cruzamentos maria passou em X e em Y
# cruzamentos em X |Xm-Xr| + cruzamentos em Y |Ym-Yr|
cruzamentos = abs(Xm-Xr) + abs(Ym-Yr)
print(cruzamentos)