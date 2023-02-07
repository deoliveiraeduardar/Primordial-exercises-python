from num2words import num2words

# Escrevendo por extenso
# Gerando lista
lista = []

for d in range(0, 20+1):
    n_extenso = num2words(d, lang='pt-br').title()
    lista.append(n_extenso)
print('')

# Converter lista em tulpa
print(f'Lista:', lista)
tudo_na_tulpa = tuple(lista)
print(f'Tulpa: ', tudo_na_tulpa)
