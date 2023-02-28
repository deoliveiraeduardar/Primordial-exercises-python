temporario = []

lista_unica = []

pares = []
impares = []

while True:
    temporario.append(int(input('Digite o valor: ')))
    lista_unica.append(temporario[:])
    print(f'Printando temporário: {temporario}')
    print(f'Printando lista_unica: {lista_unica}')

    if temporario % 2 == 0:
        print(f'{temporario} é um número par')
        pares.append(temporario[:])
        print(f'Printando lista de pares: {pares}')
    else:
        print(f'{temporario} é um número ímpar')
        impares.append(temporario[:])
        print(f'Printando lista de ímpares: {impares}')

    temporario.clear()
    print('Chegamos após temporario clear')
    print(f'Printando lista_unica máximo : {max(lista_unica)}')
    print(f'Printando lista_unica minimo : {min(lista_unica)}')

    print('')
