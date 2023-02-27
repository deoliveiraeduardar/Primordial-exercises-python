print('Vamos verificar se a sua expressão matemática está com a quantidade e ordem certa de parênteses.')
print('=====' * 18)
print('')

expr = str(input('Digite a expressão matemática com parênteses: '))
pilha = []

for simbolo in expr:
    if simbolo == '(':
        pilha.append('(')

    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('Sua epressão é válida!')
else:
    print('Sua expressão é inválida!')
