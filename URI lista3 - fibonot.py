#1 , 1, 2, 3, 5, 8, 13, 21, 34
#n1 n2  nf
k = int(input())
nf = 0
n1 = 0
n2 = 1
fib = []
#print(fib)
fibonot = []
for f in range(24): #gerador de Fibonacci 
    nf =  n1 + n2
    fib.append(nf)
    n1 = n2
    n2 = nf
#-------------------------
for fn in range(k+(k+5)):
    if fn not in fib:
        fibonot.append(fn)
print(fibonot[k])
