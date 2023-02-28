dado_temp = []
# dado é lista temporária
principal = list()
quantas_pessoas = 0
maior = menor = 0

while True:
    dado_temp.append(str(input('Nome: ')))
    dado_temp.append(float(input('Peso: ')))
    quantas_pessoas += 1

    if len(principal) == 0:
        maior = menor = dado_temp[1]

    else:
        if dado_temp[1] > maior:
            maior = dado_temp[1]
        if dado_temp[1] < menor:
            menor = dado_temp[1]

    # Para criar ligação só digito temp. Para gerar cópia digito [:]
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
print('Já fora do break...')

print('==='*25)
print(f'PRINTANDO DADO_TEMPORÁRIO: {dado_temp}')
print(f'PRINTANDO LISTA FINAL DE PRINCIPAL: {principal}')
print(f'')

print(f'Maior peso: {maior}kg. Peso de ', end='')
for peso in principal:
    if peso[1] == maior:
        print(f'[{peso[0]}] ', end='')
print()

print(f'Menor peso: {menor}kg. Peso de ', end='')
for peso in principal:
    if peso[1] == menor:
        print(f'[{peso[0]}] ', end='')


print('')
print(f'Quantidade de pessoas cadastradas com contador: {quantas_pessoas}')
print(f'Quantidade de pessoas cadastradas com len: {len(principal)}')

# Se eu colocar sem o [:] quando printo galera, ele triplica a lista
