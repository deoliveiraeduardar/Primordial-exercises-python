print('Vamos verificar se a sua expressão matemática está com a quantidade e ordem certa de parênteses.')
print('=====' * 18)
print('')

frase = str(input('Digite a expressão matemática com parênteses: '))
list(frase)
print(f'Essa é a frase: {frase}')
print(f'Quantidade de caracteres: {len(frase)}')
print('')

print(frase)

print(f'O primeiro parêntese aberto ocorre na posição: {frase.index('(')}'))
print('O primeiro parênteses aberto ocorre em: {}'.format(frase.index('(')))
frase.index('(')

# USAR LEN
# LOACALIZAR O LOCAL ONDE TEM O PRIMEIRO PARÊNTESES
#D
