matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para a posição [{linha}, {coluna}]: '))

print('====' * 20)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[ {matriz[linha][coluna]:^5} ]', end='')

        if matriz[linha][coluna] % 2 == 0:
            spar += matriz[linha][coluna]

        if coluna == 2:
            scol += matriz[linha][2]
    print()

print('====' * 20)
print('')
print(f'Soma de todos os pares: {spar}')
print(f'Soma dos valores da 3ª coluna: {scol}')

# Tá pegando a linha correta
print(f'Valores da 2ª linha: {matriz[1]}')
matriz[1].sort()
print(f'Valor máximo da 2ª linha com sort: {matriz[1][2]}')
