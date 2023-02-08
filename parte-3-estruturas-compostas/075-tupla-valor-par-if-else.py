tupla = (int(input('Digite um número: ')),
     int(input('Digite mais número: ')),
     int(input('Digite outro número: ')),
     int(input('Digite o último número: ')))
lista = []

print('')
if 9 in tupla:
    print(f'Vezes que apareceram o nº 9: {tupla.count(9)}')
else:
    print('O número 9 não apareceu nenhuma vez.')

if 3 in tupla:
    print(f'Vezes que apareceram o nº 9: {tupla.index(3) + 1}')
else:
    print('O número 3 não apareceu nenhuma vez.')

print('Os números pares digitados foram: ', end='')

for numero in tupla:
    if numero % 2 == 0:
        print(numero, end=' ')
