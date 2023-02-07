from random import randint

lista = []

quantidade = int(input('Digite quantos números aleatórios você quer gerar: '))
print('')

for d in range(0, quantidade):
    elemento = randint(0, 100)
    lista.append(elemento)

# Converter lista em tulpa
tulpa = tuple(lista)
print(f'Cinco números aleatórios gerados:: ', tulpa)
print(f'Números em ordem alfabética: {sorted(tulpa)}')
print('')

print(f'Menor nº na tupla: {min(tulpa)}')
print(f'Maior nº na tupla: {max(tulpa)}')

