quantidade = int(input('Digite quantos números você quer inserir: '))
lista = list()
# Se eu fizer lista = [] não funciona

for d in range(0, quantidade):
    numero = int(input('Digite o número: '))
    if numero not in lista:
        lista.append(numero)
        print('Como o número não está na lista, vou adicioná-lo')
        print(lista)

    else:
        print('Ops, número já digitado. Não vou adicionar.')

print(f'LISTA NA ORDEM ORIGINAL: {lista}')
lista.sort()
print(f'LISTA CRESCENTE: {lista}')
