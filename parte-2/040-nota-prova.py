print('---'*14)
print('SAIBA A CATEGORIA NA NATAÇÃO')
print('---'*14)

nome = str(input('Digite o nome do competidor: ')).title()
idade = int(input('Digite o ano de nascimento: '))
ano = int(input('Digite o ano que pretende competir: '))
idade = ano - idade
print(f'{nome} tem {idade} anos.')
print('')

if idade <= 9:
    print(f'Como {nome} tem {idade} anos, irá competir na categoria \033[36mMIRIM\033[m.')

elif idade > 9 and idade <= 14:
    print(f'Como {nome} tem {idade} anos, irá competir na categoria \033[36mINFANTIL\033[m.')

elif idade > 14 and idade <= 19:
    print(f'Como {nome} tem {idade} anos, irá competir na categoria \033[36mJUNIOR\033[m.')

elif idade > 19 and idade <= 20:
    print(f'Como {nome} tem {idade} anos, irá competir na categoria \033[36mSÊNIOR\033[m.')

elif idade > 20:
    print(f'Como {nome} tem {idade} anos, irá competir na categoria \033[36mMASTER\033[m.')