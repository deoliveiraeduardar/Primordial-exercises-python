galera = []
dado = []
# Dado é  temprário
totalmaior = totalmenor = 0

for d in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    # Colocar [:] pra gerar cópia de dados
    galera.append(dado[:])
    dado.clear()
    print('')

print(f'Lista total: {galera}')

for pessoa in galera:
    if pessoa[1] >= 18:
        print(f'{pessoa[0].title()} é maior de idade')
        totalmaior += 1
    else:
        print(f'{pessoa[0]} é mrenor de idde')
        totalmenor += 1

print('')
print(f'Temos {totalmaior} maiores de idade e {totalmenor} menores de idade.')

