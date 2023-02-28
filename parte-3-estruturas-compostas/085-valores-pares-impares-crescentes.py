temporario = []

lista_unica = []

pares = []
impares = []

while True:
    temporario.append(float(input('Digite o valor: ')))
    lista_unica.append(temporario[:])
    print(f'Printando temporário: {temporario}')
    temporario.clear()
    print('')
