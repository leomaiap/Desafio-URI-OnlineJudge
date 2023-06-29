n = input().split()
n1, n2, n3, n4 = float(n[0]), float(n[1]), float(n[2]), float(n[3])
med = ((n1*2)+(n2*3)+(n3*4)+(n4*1))/10
print('Media: {:.1f}'.format(med))
if med >= 7:
    print('Aluno aprovado.')
elif med < 5:
    print('Aluno reprovado.')
elif 5 <= med <= 6.9:
    print('Aluno em exame.')
    ex = float(input())
    print('Nota do exame: {:.1f}'.format(ex))
    med2 = (med + ex) / 2 
    if med2 >= 5:
        print('Aluno aprovado.')
        print('Media final: {:.1f}'.format(med2))
    elif med2 <= 4.9:
        print('Aluno reprovado.')
        print('Media final: {:.1f}'.format(med2))
