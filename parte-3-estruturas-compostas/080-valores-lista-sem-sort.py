lista = list()

for c in range(1, 5 + 1):
    numeros = int(input(f' Digite o {c}º número: '))
    print(f'LISTA: {lista}')


    # Ou lista[-1]
    if c == 0:
        lista.append(numeros)

    if numeros > lista[-1]:
        lista.append(numeros)

    else:
        pos = 0
        while pos < len(lista):
            if numeros <= lista[pos]:
                lista.insert(pos, numeros)
                break
            pos += 1
    print('===' * 30)
    print(f'Os valorse igitados em ordem crescente sem sort foram: {lista}')
