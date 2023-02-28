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

        if linha == 1:
            

    print()

print('====' * 20)
print(f'Soma de todos os pares: {spar}')
print(f'Soma dos valores da terceira coluna: {scol}')
