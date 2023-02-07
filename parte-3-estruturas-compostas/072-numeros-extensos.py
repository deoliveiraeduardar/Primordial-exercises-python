from num2words import num2words

numero = int(input('Digite um número: '))
extenso= num2words(numero, lang='pt-br')
print(f'Número por extenso: {extenso}')

# lista = []

# Escrevendo por extenso
# Gerando lista
# for d in range(0, 20+1):
    # n_extenso = num2words(d, lang='pt-br').title()
    # lista.append(n_extenso)
    # print('')
    # print(f'Fazendo a lista aparecer: ')
# print('')

# Converter lista em tulpa
# print(f'Lista:', lista)
# tudo_na_tulpa = tuple(lista)
# print(f'Tulpa: ', tudo_na_tulpa)

# Usuário, digite um número que você quer ver por extenso
# numero_usuario = int(input('Digite o número que você quer ver por extenso: '))
