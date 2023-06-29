'''
 se o salário for R$ 3002.00, a taxa que incide é de 8% apenas sobre
 R$ 1000.00, pois a faixa de salário que fica de R$ 0.00 até R$ 2000.00
 é isenta de Imposto de Renda. No exemplo fornecido (abaixo), a taxa é de
 8% sobre R$ 1000.00 + 18% sobre R$ 2.00, o que resulta em R$ 80.36 no total.
 O valor deve ser impresso com duas casas decimais.
'''
renda = float(input())

if renda <= 2000:
    print('Isento')
elif 2000.01 <= renda <= 3000:
    taxa8 = renda-2000
    imposto1 = taxa8*0.08
    print('R$ {:.2f}'.format(imposto1))
    #print(taxa8)
elif 3000.01 <= renda <= 4500:
    taxa8 = 1000*0.08
    taxa18 = renda-3000
    imposto2 = (taxa8)+(taxa18*0.18)
    print('R$ {:.2f}'.format(imposto2))
    #print(taxa8, taxa18)
elif renda > 4500:
    taxa8 = 1000*0.08
    taxa18 = 1500*0.18
    taxa28 = renda-4500
    imposto3 = (taxa8+taxa18)+(taxa28*0.28)
    print('R$ {:.2f}'.format(imposto3))
    #print(taxa8, taxa18, taxa28)
