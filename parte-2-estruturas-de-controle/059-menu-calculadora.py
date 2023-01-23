import time
print('----'*5, 'MINI CALCULADORA DE DOIS VALORES', '----'*5)
print('')


n1 = int(input('\033[1mPrimeiro valor:\033[m '))
n2 = int(input('\033[1mSegundo valor:\033[m '))
opcao = 0

while opcao != 5:
    print('''Menu
        [1] somar
        [2] multiplicar
        [3] qual é o maior
        [4] digitar novos números
        [5] sair do programa''')
    opcao = int(input('\033[1mDigite a opção desejada:\033[m '))

    if opcao == 1:
        print(f'A soma de {n1} e {n2} é {n1+n2}')
        time.sleep(2)

    elif opcao == 2:
        print(f'A multiplicação de {n1} e {n2} é {n1*n2}')
        time.sleep(2)

    elif opcao == 3:
        if n1 > n2:
            print(f'O número maior é {n1}')
        if n1 < n2:
            print(f'O número maior é {n2}')
        else:
            print(f'Os dois números são iguais.')
        time.sleep(2)

    elif opcao == 4:
        print('Informe os números novamente.')
        n1 = int(input('\033[1mPrimeiro valor:\033[m '))
        n2 = int(input('\033[1mSegundo valor:\033[m '))
        time.sleep(2)

    elif opcao == 5:
        print('Finalizando')

    else:
        print('Opção inválida. Tente novamente.')
    print('==='*10)
    time.sleep(1)

print('Fim do programa. Volte quando precisar!')
