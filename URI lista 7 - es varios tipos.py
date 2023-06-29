import sys
entrada = input().split(" ",3)
a = int(entrada[0])
b = float(entrada[1])
c = entrada[2]
d = entrada[3]

saidatab = open(tab, r+, 0)
saidatab.write(f'{a}\t{b:.6f}\t{c}\t{d}')
saidatab.close()

tab = saidatab.readline()

print('{}{:.6f}{}{}'.format(a, b, c, d))
print(tab)
print("%10d%10.6f%10c%10s" % (a, b, c, d))
