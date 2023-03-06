from random import randint
cont = 0
lista = list()
while True:
    num = randint(1, 60)
    if num not in lista:
        lista.append(num)
        cont += 1
    if cont >= 6:
        print('Entrou no break')
        break


# Quantos jogos vai gerar
# Cada jogo tem 6 numeros diferentes em cada jogo
# Numeros: 1 a 60
# Tudo cadastrado em lista composta

while True:
    quantidade = int(input('Digite quantos jogos você quer fazer: '))
    jogos2 = [], * quantidade
    print(jogos2)