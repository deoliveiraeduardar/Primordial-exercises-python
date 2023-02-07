resto3 = 0
soma3 = 0
contador3 = 0
resto5 = 0
soma5 = 0
contador5 = 0

numero = int(input('Digite o número que você quer verificar: '))

print('-----' * 5, 'CALCULANDO PARA 3', '-----' * 5)
for d in range(1, numero):
    resto3 = d % 3
    if resto3 == 0:
        soma3 += d
        contador3 += 1
        print(f'O numero {d} é divisível por 3')


print('-----' * 5, 'CALCULANDO PARA 5', '-----' * 5)
for d in range(1, numero):
    resto5 = d % 5
    if resto5 == 0:
        soma5 += d
        contador5 += 1
        print(f'O numero {d} é divisível por 5')

print('')
print('======' * 5, 'CALCULO TOTAL', '======' * 5)
print(f'- Total de números divisíveis por 3: {contador3}')
print(f'- Soma total dos {contador3} números: {soma3} ')
print('')

print(f'- Total de números divisíveis por 5: {contador5}')
print(f'- Soma total dos {contador5} números: {soma5} ')
print('')

print(f'Total de números divisíveis por 3 e 5: {contador3 + contador5}')
print(f'Soma total dos {contador3 + contador5} números: {soma3 + soma5}')
