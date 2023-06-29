idade = int(input())
a = idade//365
r = idade%365
m = r//30
d = r%30
print('{} ano(s)'.format(a))
print('{} mes(es)'.format(m))
print('{} dia(s)'.format(d))