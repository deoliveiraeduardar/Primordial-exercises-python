temporario = []
lista_unica = []

pares = []
impares = []

valor = 0

while True:
    valor = float(input('Digite um valor: '))

    if valor % 2 == 0:
        print(f'{valor} é um número par')
        pares.append(valor[:])
        print(f'Printando lista de pares: {pares}')

    else:
        print(f'{valor} é um número ímpar')
        impares.append(valor[:])
        print(f'Printando lista de ímpares: {impares}')


    temporario.append(int(input('Digite o valor: ')))
    lista_unica.append(temporario[:])
    print(f'Printando temporário: {temporario}')
    print(f'Printando lista_unica: {lista_unica}')

    temporario.clear()
    print('Chegamos após temporario clear')
    print(f'Printando lista_unica máximo : {max(lista_unica)}')
    print(f'Printando lista_unica minimo : {min(lista_unica)}')

    print('')
