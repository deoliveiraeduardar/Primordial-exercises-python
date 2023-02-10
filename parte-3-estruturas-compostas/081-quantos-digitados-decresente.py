lista = list()
quantidade = 0

while True:
    valor = int(input('\033[1mDigite um valor: \033[m'))
    lista.append(valor)

    print('   Caso queira continuar digitando, digite S para sim e N para não.')
    escolha = str(input('\033[1mDigite a sua opção: \033[m')).upper()

    while escolha not in 'SN':
        print('   Dados inválidos.')
        print('')

        escolha = str(input('\033[1mDigite novamente: \033[m')).upper()
    if escolha in 'N':
        print('Entrou no break')
        quantidade = len(lista)
        print(f'Lista decrescente: {lista.sort(reverse=True)}')

        break


print('')
print('PASSOU DO WHILE TRUE.')
print(f'Quantidade de elementos: {quantidade}')
