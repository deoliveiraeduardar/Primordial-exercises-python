listagem = ('Macbook', 50000,
            'Iphone 15', 30000,
            'Ipad', 10000,
            'Apple watch Ultra', 7000,
            'Airpod', 7500.50,
            'Apple tv', 16000)

print('=' * 62)
print(f'{"LISTAGEM DE PREÇOS":^62}')
print('=' * 62)

for posicao in range(0, len(listagem)):
    if posicao % 2 == 0:
        print(f'{listagem[posicao]:.<50}', end='')
    else:
        print(f'R${listagem[posicao]:>10.2f}')
print('===' * 10)


# quantidade = int(input('Digite quantos produtos você quer inserir: '))
# lista = []

# for w in range(0, quantidade):
    # nome = str(input('Digite o nome do produto: ')).title()
    # preco = float(input('Digite o preço do produto: '))
    # lista.append(nome), lista.append(preco)
    # print(lista)

# Converter lista em tulpa
# tulpa = tuple(lista)

# contador = 0

# for w in range(1, quantidade + 1):
    # print(f'{tulpa[0 + contador]}')
    # contador += 1
