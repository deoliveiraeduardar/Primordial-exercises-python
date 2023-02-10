lista = []

for d in range(0, 5):
    numeros = int(input('Digite um número: '))
    lista.append(numeros)

print('')
print(f'Você criou a lista: {lista}')
print(f'Maior número(posição {lista.index(max(lista))}): {max(lista)}')
print(f'Menor número (posição {lista.index(min(lista))}): {min(lista)}')
