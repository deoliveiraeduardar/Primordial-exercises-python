print('Vamos verificar se a sua expressão matemática está com a quantidade e ordem certa de parênteses.')
print('=====' * 18)
print('')

expr = str(input('Digite a expressão matemática com parênteses: '))
lista_verificadora = []

for simbolo in expr:
    if simbolo == '(':
        # Quando tiver parêntese aberto, adiciona um ( na lista_verificadorr.
        lista_verificadora.append('(')

    elif simbolo == ')':
        if len(lista_verificadora) > 0:
            # Caso a lista não esteja vazia, remove o último elemento da lista_verificadora
            lista_verificadora.pop()
        else:
            # Caso a lista estiver vazia, um ) é adicionado na lista_verificadora.
            lista_verificadora.append(')')
            break


if len(lista_verificadora) == 0:
    # Cada parêntese aberto foi fechado
    print('Sua epressão é válida!')
else:
    # Ao menos um parêntese aberto não foi fechado
    print('Sua expressão é inválida!')
