matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para a posição [{linha}, {coluna}]: '))

print('====' * 20)
for linha in range(0, 3):
    for coluna in range (0, 3):
        print(f'[ {matriz[linha][coluna]} ]', end='')
    print()
