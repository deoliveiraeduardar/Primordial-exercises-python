print('====='*15)
print('SAIBA SE O ANO É BISSEXTO')
print('====='*15)

#DIVISIVEL POR 4
#fazer n1%n2 e o resto deve ser 0
#se for 0 é bissexto
n = int(input('Digite o ano: '))
nn = str(n)
print('')

if '00' in nn:
    a = n%400
    if a == 0:
        print('Como é divisivel por 400, é bissexto.')
    else:
        print('Como não é divisível por 400, não é bissexto.')


#NÃO TERMINADO EM 00
else:
    a = n%4
    if a == 0:
        print('Como é divisível por 4, é um ano bissexto.')
    if a != 0:
        print('Como não é divisível por 4, não é um ano bissexto.')





#SE O RESETO NÃO FOR ZERO:
#dividir n1 por 100
#se a divisao não for exata: é bissexto