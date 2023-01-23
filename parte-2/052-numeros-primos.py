print('-----'*15)
print('DESCUBRA SE É UM NÚMERO PRIMO')
print('-----'*15)

n = int(input('Digite o número: '))
resto1 = n % 1
cont = 0
#print(f'Dividindo {n} por 1, o resto é {resto1}')
print('')


for d in range(1,n):
    resto = n % d
    #print(f'Dividindo {n} por {d} o resto é {resto}')
    #print('')

    if resto == 0:
        cont += 1
        #print(f'O resto {cont}')
if cont == 1:
    print(f'O número {n} é um número primo, pois ele é divisível somente por 1 e por ele mesmo.')
else:
    print(f'O número {n} não é um número primo, pois ele é divisível por mais {cont} números além dele mesmo.')