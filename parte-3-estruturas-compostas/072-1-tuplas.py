print('====' * 5, 'TUPLAS', '====' * 5)
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata frita')

print('\033[1mFazendo com   for cont in range(0, len(lanche):\033[m')
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')

print('')
print('\033[1mFazendo com   for comida in lanche:\033[m')
for comida in lanche:
    print(f'Eu vou comer {comida}')

print('')

print('\033[1mFazendo pra gerar a posição, com   for cont in range(0, len(lanche)):\033[m')
print('*não tem como gerar a posição usando, diretamente, in')
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

print('')
print('\033[1mFazendo pra gerar a posição, com   for pos, comida in enumerate(lanche):\033[m')
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer comida {comida} na posição {pos}')

print()
print('  - Total de índices de lanche:', len(lanche))
print('  - Comi na proporção correta')
print('  - Mostrando em ordem alfabética com   print(sorted(lanche)): ')
print(sorted(lanche))

