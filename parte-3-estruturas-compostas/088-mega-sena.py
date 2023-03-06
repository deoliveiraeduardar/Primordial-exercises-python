from random import randint
print('=='*25)
print('              JOGA NA MEGA SENA              ')
print('=='*25)

lista = list()
jogos = list()
quant = int(input('Digite jogos você quer que eu sorteie: '))
tot = 1

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
    tot += 1
print('')

print('----' * 3, f'Sorteando {quant} jogos', '---' * 3)
for i, l in enumerate(jogos):
    
print(f'Os números sorteados foram {jogos}')


# Quantos jogos vai gerar
# Cada jogo tem 6 numeros diferentes em cada jogo
# Numeros: 1 a 60
# Tudo cadastrado em lista composta
