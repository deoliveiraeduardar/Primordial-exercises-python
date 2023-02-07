from num2words import num2words

# CRIAÇÃO DE LISTA POR EXTENSO A PARTIR DO FOR
lista = []

for d in range(0, 20+1):
    n_extenso = num2words(d, lang='pt-br').title()
    lista.append(n_extenso)
print('')

# CONVERSÃO DA LISTA PARA TULPA
# print(f'Lista:', lista)
tulpa = tuple(lista)
# print(f'Tulpa: ', tulpa)

# WHILE
while True:
    n_usuario = int(input('Digite um número de 0 a 20: '))
# FAZENDO O USUÁRIO DIGITAR UM NÚMERO VÁLIDO
    if n_usuario < 0 or n_usuario > 20:
        print('Você não digitou um número válido.')
        print('')
        n_usuario = int(input('Tente de novo. Digite um número de 0 a 20: '))

    if 0 <= n_usuario <= 20:
        print('O número por extenso é: ', tulpa[n_usuario])
        break
