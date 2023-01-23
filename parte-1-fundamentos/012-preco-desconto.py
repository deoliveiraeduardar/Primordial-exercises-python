print('---'*30)
print('CALCULE O PREÇO DE UM PRODUTO COM DESCONTO')
print('---'*30)

produto = str(input('Qual o nome do produto que você pretende comprar? '))
preco = float(input('Qual o preço dele? '))
desconto = float(input('Digite a porcentagem do desconto (sem usar o símbolo %):  '))
df= (100-desconto)/100
calculo = preco*df
print(calculo)
print('')

print(f'Com o desconto de {desconto}% você pagará o valor de R$ {calculo} pela {produto}.')