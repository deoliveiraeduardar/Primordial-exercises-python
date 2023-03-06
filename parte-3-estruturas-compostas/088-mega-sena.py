from random import randint
lista = list()
cont = 0
print('-'*30)
print('        JOGA NA MEGA SENA        ')
print('-'*30)

while True:
    num = randint(1, 60)
    if num not in lista:
        lista.append(num)
        cont += 1
    if cont >= 6:
        print('Entrou no break')
        break
lista.sort()
print(f'Os números sorteados foram {lista}')


# Quantos jogos vai gerar
# Cada jogo tem 6 numeros diferentes em cada jogo
# Numeros: 1 a 60
# Tudo cadastrado em lista composta
