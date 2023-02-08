
n1 = float(input('Digite um número: '))
n2 = float(input('Digite mais um número: '))
n3 = float(input('Digite outro número: '))
n4 = float(input('Digite o último número: '))




lista = []

while True:
    for d in range(0, quantidade + 1):
        n = float(input('Digite o número: '))
        lista.append(n)
    break

# Converter lista em tulpa
print(f'Lista:', (lista))
tupla = tuple(lista)
print(f'Tulpa: ', tupla)
