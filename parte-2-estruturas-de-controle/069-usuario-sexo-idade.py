import time
sexo = ' '
contador_idade = 0
contador_homens = 0
contador_mulheres19 = 0

while True:
    nome = str(input('Digite o nome da pessoa: ')).title()
    print(nome)
    idade = int(input('Digite a idade: '))
    sexo = str(input('Levando em conta M pra masculino e F para feminino, digite a opção: ')).upper()

    while sexo not in 'MF' and sexo not in '':
        sexo = str(input('Levando em conta M pra masculino e F para feminino, digite a opção: ')).upper()

    if sexo == 'M':
        contador_homens += 1

    if idade > 18:
        contador_idade += 1

    if sexo == 'F' and idade < 20:
        contador_mulheres19 += 1

    print('Você quer adicionar mais uma pessoa? Para sim digite S. Para não digite N. ')
    time.sleep(0.5)
    escolha = input('Digite sua escolha: ').upper()

    while escolha not in 'SN':
        print('')
        print('Você não digitou uma opção válida.')
        time.sleep(0.5)
        print('Quer adicionar mais pessosa? Para sim digite S. Para não digite N.')
        time.sleep(0.5)
        escolha = str(input('Digite sua escolha: ')).upper()

    if escolha == 'S':
        print('-------' * 8)
    if escolha == 'N':
        print('')
        print('Antes de encerrar o programa, vamos ver as informações:')
        time.sleep(1)

        print(f'  -Tem {contador_homens} homens cadastrdos.')
        time.sleep(1)
        print(f'  -Tem {contador_idade} pessoas com mais de 18 anos.')
        time.sleep(1)
        print(f'  -Tem {contador_mulheres19} mulheres com mais de 18.')
        time.sleep(1)
        print('')
        print('Programa encerrado.')
        break
