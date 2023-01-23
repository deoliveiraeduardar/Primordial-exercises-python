import time
print('Digite os números, saiba a média e os valores menor e maior')
print('----'*20)

media = 0
menor = 0
maior = 0
n = 0

decisao = ''
contador = 0
soma = 0

while n >= 0 or n < 0:
    print('===='*11)
    print('''Levando em conta as seguintes informações
    Inserir um número: digite 1
    Não inserir: digite 2
    ''')
    time.sleep(0.5)

    decisao = str(input('Digite a opção desejada: '))
    print('')

    if decisao == '1':
        n = float(input('Digite um número: '))
        contador += 1
        soma += n
        media = soma / contador
        print(f'QUANTIDADE INSERIDA: {contador} numeros')
        print(f'SOMA: {soma}')
        print(f'MÉDIA: {media}')
        time.sleep(2)


    elif decisao == '2':
        print(f'Certo. Vamos fazer o cálculo somente com {contador} números:')
        print(f'         Soma: {soma}')
        print(f'         Média: {media}')
        time.sleep(2)
        break

    else:
        print('Informe a opção desejada novamente.')
        print('')
        time.sleep(2)

