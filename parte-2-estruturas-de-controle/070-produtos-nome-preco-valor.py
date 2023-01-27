import time
print('-=-=-=' * 5, 'ORGANIZAÇÃO DE COMPRAS DE PRODUTOS', '-=-=-=' * 5)

total = 0
contador_1000 = 0

menor = 0
contador = 0
nome_barato = 0

while True:
    resposta = ' '
    produto = str(input('Digite o nome do produto: ')).lower()
    preco = float(input(f'Digite o valor de {produto}: R$ '))

    contador += 1
    total += preco

    if preco > 1000:
        contador_1000 += 1
    print('')

    if contador == 1 or preco < menor:
        menor = preco
        nome_barato = produto

    print('Você quer adicionar mais um prduto?')
    while resposta not in 'SN':
        resposta = str(input('Caso sim digite S, caso não digite N. Digite sua opção: ')).upper().strip()
    print('')
    time.sleep(1)

    if resposta == 'N':
        break

print('Finalizando o programa...')
time.sleep(1)
print('')

print(f'Gasto total da compra: R$ {total:.2f}.')
time.sleep(0.5)
print(f'Produtos que custam mais de R$ 1000: {contador_1000}')
time.sleep(0.5)
print(f'Valor do produto mais barato: R$ {menor}')
time.sleep(0.5)
print(f'Nome do produto mais barato: {nome_barato}')
time.sleep(0.5)
print('Programa finalizado.')
