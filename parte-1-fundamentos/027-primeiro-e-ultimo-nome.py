print('# # '*10)
print('ANALISANDO O NOME COMPLETO')
print('# # '*10)

nome = str(input('Digite o nome completo: ')).title()
lista = nome.split()

print(f'O primeiro nome é {lista[0]}')
print('O último nome é {}'.format(lista[-1]))
