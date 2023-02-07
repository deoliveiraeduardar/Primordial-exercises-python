print('====' * 5, 'TUPLAS', '====' * 5)
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata frita')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')


for comida in lanche:
    print(f'Eu vou comer {comida}')

print('Total de índices de lanche:', len(lanche))
print('  - Comi na proporção correta')
