num = 0
lista = [[], [], []]

# LINHA 0
for d in range(0, 3):
    num = int(input(f'Digite o número da posição [0, {d}]: '))
    lista[0].append(num)
    print(f'Printando lista: {lista}')

# LINHA 1
for d in range(0, 3):
    num = int(input(f'Digite o número da posição [1, {d}]: '))
    lista[1].append(num)
    print(f'Printando lista: {lista}')


# LINHA 2
for d in range(0, 3):
    num = int(input(f'Digite o número da posição [2, {d}]: '))
    lista[2].append(num)
    print(f'Printando lista: {lista}')

print('')
print(f'[ {lista[0][0]} ]', '' * 6, f'[ {lista[0][1]} ]', '' * 6, f'[ {lista[0][2]} ]')
print(f'[ {lista[1][0]} ]', '' * 6, f'[ {lista[1][1]} ]', '' * 6, f'[ {lista[1][2]} ]')
print(f'[ {lista[2][0]} ]', '' * 6, f'[ {lista[2][1]} ]', '' * 6, f'[ {lista[2][2]} ]')
