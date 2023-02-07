from random import randint

lista = []

quantidade = int(input('Digite quantos números aleatórios você quer gerar: '))
for d in range(0, quantidade):
    elemento = randint(0,100)
    lista.append(elemento)

# Converter lista em tulpa
print(f'Lista:', lista)
tudo_na_tulpa = tuple(lista)
print(f'Cinco números aleatórios gerados:: ', tudo_na_tulpa)
