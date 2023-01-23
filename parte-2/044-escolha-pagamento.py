print('---'*14)
print('ESCOLHA A CONDIÇÃO DE PAGAMENTO')
print('---'*14)

produto = str(input('Digite o nome do produto: ')).title()
preco = float(input('Digite o valor do produto: '))
print('')
print('''\033[1mLevando em conta as seguintes informações\033[m:
À vista, em dinheiro ou cheque, com 10% de desconto: digite 1
À vista, no cartão, com 5% de desconto: digite 2
Até 2x no cartão sem juros: digite 3
A partir de 3x no cartão com 20% de juros: digite 4''')
print('')
opcao = int(input('Digite o número da forma de pagamento escolhida: '))
print('')

if opcao == 1:
    valor = preco*0.90
    print('Você escolheu pagar à vista, em dinheiro ou cheque, com 10% de desconto.')
    print(f'O valor pago por {produto} é de R$ {valor}.')

if opcao == 2:
    valor = preco*0.95
    print('Você escolheu pagar à vista, no cartão, com 5% de desconto.')
    print(f'O valor pago por {produto} é de R$ {valor}.')

if opcao == 3:
    print('Você escolheu pagar 2x no cartão sem juros.')
    print(f'O valor pago por {produto} é o mesmo original de R$ {preco}.')

if opcao == 4:
    valor = preco*1.2
    print('Você escolheu pagar a partir de 3x no cartão com 20% de juros.')
    print(f'O valor pago por {produto} é de R$ {valor}.')
