print('Vamos verificar se a sua expressão matemática está com a quantidade e ordem certa de parênteses.')
print('=====' * 18)
print('')
# Solução:

expr = str(input('Digite a expressão matemática com parênteses: '))
lista_verificadora = []

for simbolo in expr:
    if simbolo == '(':
        lista_verificadora.append('(')
        # Quando tiver parêntese aberto, adicionar ( na lista_verificadorr.

    elif simbolo == ')':
        if len(lista_verificadora) > 0:
            lista_verificadora.pop()
        else:
            lista_verificadora.append(')')
            break
        # Quando tiver parêntese fechado, remover da lista_verificadorr.


if len(lista_verificadora) == 0:
    print('Sua epressão é válida!')
else:
    print('Sua expressão é inválida!')
