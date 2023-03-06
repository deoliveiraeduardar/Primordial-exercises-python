from random import randint
print('-'*35)
print('        JOGA NA MEGA SENA        ')
print('-'*35)

lista = list()
jogos = []
quant = int(input('Digite jogos você quer que eu sorteie: '))
tot = 0

while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    print(f'Os números sorteados foram {lista}')


# Quantos jogos vai gerar
# Cada jogo tem 6 numeros diferentes em cada jogo
# Numeros: 1 a 60
# Tudo cadastrado em lista composta
