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

