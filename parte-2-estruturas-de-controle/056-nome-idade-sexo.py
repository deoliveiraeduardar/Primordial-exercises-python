print('====='*15)
print('SAIBA INFORMAÇÕES DE UM GRUPO: IDADE, SEXO')
print('====='*15)
print('')

n = int(input('Digite o numero de pessoas que compõe o grupo: '))

# Para média da idade do grupo
somaidade = 0
mediaidade = 0

# Para saber quantas mulheres tem menos de 20
contador_mulheres_19 = 0

# Para nome e idade do homem mais velho
idade_homem_velho = 0
nome_homem_velho = ''


for d in range(1, n + 1):
    print('----' * 5, f'{d}ª PESSOA', '----' * 5)
    # Nome
    nome = str(input(f'Digite o nome da {d}ª pessoa: ')).title()

    # Idade
    idade = int(input(f'Digite a idade de {nome}: '))
    somaidade += idade
    mediaidade = somaidade / n
    print('')

    # Sexo
    print('  Levando em conta as seguintes informações:\n  sexo feminino: 1 \n  sexo masculino: 2')
    sexo = int(input(f'Para {nome}, digite o número correspondete ao sexo: '))
    print('')

    ## Para sexo feminino (1) e mais de 20 anos:
    if idade <= 19 and sexo == 1:
        contador_mulheres_19 += 1
    else:
        contador_mulheres_19 += 0

    ## Para sexo masculino (2) mais velho:
    if d == 1 and sexo == 2: # Se d for a primeira pessoa (d == 1) e o sexo for masculino (2)
        idade_homem_velho = idade
        nome_homem_velho = nome
    if sexo == 2 and idade > idade_homem_velho:
        idade_homem_velho = idade
        nome_homem_velho = nome


# Média da idade do grupo
print(f'\033[1m- A média das idades é: {mediaidade:.2f}')

# Nome e idade do homem mais velho
print(f'- O homem mais velho tem {idade_homem_velho} anos e o nome dele é {nome_homem_velho}.')

# Sabendo mulheres com menos de 20 anos
print(f'- Há {contador_mulheres_19} mulheres com menos de 20 anos.\033[m')

