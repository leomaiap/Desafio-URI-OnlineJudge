#grupo, classe, dieta
g = input()
c = input()
d = input()
if g == 'vertebrado':
    if c == 'ave':
        if d == 'carnivoro':
            print('aguia')
        else:
            print('pomba')
    else:
        if d == 'onivoro':
            print('homem')
        else:
            print('vaca')

if g == 'invertebrado':
    if c == 'inseto':
        if d == 'hematofago':
            print('pulga')
        else:
            print('lagarta')
    else:
        if d == 'hematofago':
            print('sanguessuga')
        else:
            print('minhoca')

