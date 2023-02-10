lista = list()
quantidade = 0

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

    if escolha in 'N':
        print('Entrou no break')
        quantidade = len(lista)

print('')
if 5 in lista:
    print(f'-  O número 5 está na lista.')
elif 5 not in lista:
    print(f'-  O número 5 não está na lista.')
print(f'-  Quantidade de elementos: {quantidade}')
lista.sort(reverse=True)
print(f'-  Lista decrescente: {lista}')
