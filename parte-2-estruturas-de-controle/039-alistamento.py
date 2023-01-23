print('---'*15)
print('SAIBA SE VOCÊ TERÁ QUE FAZER O ALISTAMENTO MILITAR')
print('---'*15)

nome = str(input('Digite o nome da pessoa: ')).title()
print(nome)
anon = int(input('Digite o ano do nascimento: '))
anoa = int(input('Digite o ano do alistamento: '))
idade = anoa-anon
print('')
print(f'Isso significa que {nome} tem {idade} anos.')
alistamento = anon+18

if idade < 18:
    print(f'{nome} deve fazer o alistamento no ano de {alistamento}.')

elif idade == 18:
    print(f'{nome} deve fazer o alistamento nesse ano de {alistamento}.')

else:
    print(f'Pela idade, {nome} deveria ter feito o alistamento no ano de {alistamento}.')
