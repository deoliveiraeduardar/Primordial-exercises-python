
lista = []
maior = 0
menor = 0

while True:
    valor = int(input('\033[1mDigite um valor: \033[m'))
    print('   Caso queira continuar digitando, digite S para sim e N para não.')
    escolha = str(input('\033[1mDigite a sua opção: \033[m')).upper()
    while escolha not in 'SN':
        print('   Dados inválidos.')
        print('')

        escolha = str(input('\033[1mDigite novamente: \033[m')).upper()
    if escolha in 'N':
        print('Entrou no break')
        break

print('PASSOU DO WHILE TRUE. FIM')
