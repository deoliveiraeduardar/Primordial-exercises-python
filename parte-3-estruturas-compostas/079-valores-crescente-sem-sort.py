
lista =[]
maior = 0
menor =
maior_da_lista = 0

for d in range(1, 6):
    numero = int(input(f'Digite o {d}º número: '))
    lista.append(numero)
    print(lista)

    if numero > maior:
        maior = numero

    # lista.append(numero)
    # print(f'MÁXIMO DA LISTA:{max(lista)}')
    # if numero == max(lista):

