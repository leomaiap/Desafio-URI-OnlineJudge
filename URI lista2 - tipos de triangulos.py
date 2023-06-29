abc = input().split()
list.sort(abc, key=float, reverse=True)
a, b, c = float(abc[0]), float(abc[1]), float(abc[2])
#print(abc)
#print(a, b, c)
#print((b**2)+(c**2))
if a >= b+c:
    print('NAO FORMA TRIANGULO')
elif a<0 or b<0 or c<0:
    print('NAO FORMA TRIANGULO')
elif a**2 == (b**2)+(c**2):
    print('TRIANGULO RETANGULO')
elif a**2 > (b**2)+(c**2):
    print('TRIANGULO OBTUSANGULO')
elif a**2 < (b**2)+(c**2):
    print('TRIANGULO ACUTANGULO')

if a == b and b == c and c == a:
    print('TRIANGULO EQUILATERO')
elif a == b and b != c:
    print('TRIANGULO ISOSCELES')
elif b == c and a != c:
    print('TRIANGULO ISOSCELES')
elif c == a and b != a:
    print('TRIANGULO ISOSCELES')
