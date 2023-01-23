lista = []
opcao = ''

while opcao in '12':
    n = int(input('\033[1mDigte o número: \033[m'))
    print('   Para adicionar mais um número: digitar 1')
    print('   Se não quiser adicionar mais um: digitar 2')
    opcao = str(input('\033[1mDigite a opção desejada: \033[m'))

    # Para adicionar elementos n na lista
    lista.append(n)

    if opcao == '2':
        break
print('')
print(f'Lista completa: {lista}')
print(f'   Total de elementos inseridos: {len(lista)}')
print(f'   Média dos elementos: {sum(lista) / len(lista)}')
print(f'   Maior valor: {max(lista)}')
print(f'   Menor valor: {min(lista)}')

