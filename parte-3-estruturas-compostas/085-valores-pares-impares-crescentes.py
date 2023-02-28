temporario = []

lista_unica = []

pares = []
impares = []

while True:
    temporario.append(float(input('Digite o valor: ')))
    lista_unica.append(temporario[:])
    print(f'Printando temporário: {temporario}')
    print(f'Printando lista_unica: {lista_unica}')
    temporario.clear()

    
    print(f'Printando lista_unica máximo : {max(lista_unica)}')
    print(f'Printando lista_unica minimo : {min(lista_unica)}')

    print('')
