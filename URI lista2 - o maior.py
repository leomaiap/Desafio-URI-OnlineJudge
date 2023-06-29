num = input().split()
a, b, c = int(num[0]), int(num[1]), int(num[2])
mab = (a+b+abs(a-b))/2
mabc = (mab+c+abs(mab-c))/2
print('{} eh o maior'.format(int(mabc)))
