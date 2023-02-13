lista = []
lista_pares = []
lista_impares = []

while True:
    valor = int(input('\033[1mDigite um valor: \033[m'))
    lista.append(valor)

    print('   Caso queira continuar digitando, digite S para sim e N para não.')
    escolha = str(input('\033[1mDigite a sua opção: \033[m')).upper()
    print('')

    while escolha not in 'SN':
        print('   Dados inválidos.')
        print('')
        escolha = str(input('\033[1mDigite novamente: \033[m')).upper()
        
    if valor % 2 == 0:
        lista_pares.append(valor)
        print(f'Lista pares: {lista_pares}')

    if valor % 3 == 0:
        lista_impares.append(valor)
        print(f'Lista pares: {lista_impares}')

    if escolha in 'N':
        print('Entrou no break')
        quantidade = len(lista)
        break

print(f'Lista original: {lista}')
print(f'Lista impares: {lista_impares}')
print(f'Lista pares: {lista_pares}')
