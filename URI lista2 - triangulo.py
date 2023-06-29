abc = input().split()
a, b, c = float(abc[0]), float(abc[1]), float(abc[2])

if a+b > c and b+c > a and a+c > b:
    perim = a+b+c
    print('Perimetro {:.1f}'.format(perim))
else:
    area = ((a+b)*c)/2
    print('Area {:.1f}'.format(area))
