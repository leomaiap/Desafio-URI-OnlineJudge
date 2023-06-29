n = input().split()
n1, n2, n3, n4 = float(n[0]), float(n[1]), float(n[2]), float(n[3])

avg = ((n1*2)+(n2*3)+(n3*4)+(n4*1))/10

print('Average: {:.1f}'.format(avg))

if avg >= 7:
    print('Student pass.')
elif avg < 5:
    print('Student fail.')
elif 5 <= avg <= 6.9:
    print('Student retake test')
    ex = float(input())
    print('Retake grade: {:.1f}'.format(ex))
    avg2 = (avg + ex) / 2 
    if avg2 >= 5:
        print('Student pass.')
        print('Final average: {:.1f}'.format(avg2))
    elif avg2 <= 4.9:
        print('Student fail')
        print('Final average: {:.1f}'.format(avg2))
