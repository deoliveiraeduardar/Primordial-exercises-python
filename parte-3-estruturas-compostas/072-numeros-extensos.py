from num2words import num2words

numero_humano = int(input('Digite um número entre 0 e 20:'))

lista = []

for d in range(0, 20+1):
    n_extenso = num2words(d, lang='pt-br').title()
    lista.append(n_extenso)
print('')

# Converter lista em tulpa
print(f'Lista:', lista)
tudo_na_tulpa = tuple(lista)
print(f'Tulpa: ', tudo_na_tulpa)
