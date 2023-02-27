dado_temp = []
# dado é lista temporária
principal = list()

quantas_pessoas = 0

lista_pesadas = []
lista_leves = []

while True:
    dado_temp.append(str(input('Nome: ')))
    dado_temp.append(float(input('Peso: ')))
    quantas_pessoas += 1

    principal.append(dado_temp[:])
    print(f'Printando dado: {dado_temp}')
    dado_temp.clear()
    print('')

    print('   Caso queira continuar digitando, digite S para sim e N para não.')
    escolha = str(input('Digite a sua opção: ')).upper()

    while escolha not in 'SN':
        print('   Dados inválidos.')
        print('')
        escolha = str(input('\033[1mDigite novamente: \033[m')).upper()

    if escolha in 'N':
        print('Entrando no breake')
        break

print('')
print('Saindo...')

print(f'PRINTANDO LISTA FINAL DE DADO: {dado_temp}')
print(f'PRINTANDO LISTA FINAL DE GALERA: {principal}')
print(f'')

print(f'Quantidade de pessoas cadastradas: {quantas_pessoas}')

# Se eu colocar sem o [:] quando printo galera, ele triplica a lista
