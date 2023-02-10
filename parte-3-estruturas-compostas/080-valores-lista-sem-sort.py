lista = []

for d in range(1, 5 + 1):
    numeros = int(input(f' Digite o {d}º número: '))
    print(f'LISTA: {lista}')

    # Ou lista[-1]
    if d == 0 or numeros > lista[len(lista)-1]:
        lista.append(numeros)

    else:
        pos = 0
        while pos < len(lista):
            