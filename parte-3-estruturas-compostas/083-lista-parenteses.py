print('Vamos verificar se a sua expressão matemática está com a quantidade e ordem certa de parênteses.')
print('=====' * 18)
print('')

expr = str(input('Digite a expressão matemática com parênteses: '))
verificador = []

for simbolo in expr:
    if simbolo == '(':
        verificador.append('(')

    elif simbolo == ')':
        if len(verificador) > 0:
            verificador.pop()
        else:
            verificador.append(')')
            break

if len(verificador) == 0:
    print('Sua epressão é válida!')
else:
    print('Sua expressão é inválida!')
