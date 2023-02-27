print('Vamos verificar se a sua expressão matemática está com a quantidade e ordem certa de parênteses.')
print('=====' * 18)
print('')
# Solução baseada para

expr = str(input('Digite a expressão matemática com parênteses: '))
lista_verificador = []

for simbolo in expr:
    if simbolo == '(':
        lista_verificador.append('(')
        # Quando tiver parêntese aberto, adicionar na lista_verificadorr.

    elif simbolo == ')':
        if len(lista_verificador) > 0:
            lista_verificador.pop()
        else:
            lista_verificador.append(')')
            break
        # Quando tiver parêntese fechado, remover da lista_verificadorr.


if len(lista_verificador) == 0:
    print('Sua epressão é válida!')
else:
    print('Sua expressão é inválida!')
