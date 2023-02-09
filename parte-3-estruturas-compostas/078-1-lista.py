valores = []
valores.append(5)
valores.append(4)
valores.append(9)
print(valores)
print('')

print('Mostrando a lista mais organizada')
for v in valores:
    print(f'{v}...', end='')

print('')
print('')

print('Mostrando o valor e a posição')
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')