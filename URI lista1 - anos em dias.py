idade = int(input())
a = idade//365
m = (idade//30)-(a*12)
d = (idade%365)-(m*30)
print('{} ano(s)'.format(a))
print('{} mes(es)'.format(m))
print('{} dia(s)'.format(d))