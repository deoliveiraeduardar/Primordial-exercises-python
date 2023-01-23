from random import randint
print('-----'*5, 'DESAFIO: ADIVINHE O NÚMERO QUE EU ECOLHI', '-----'*5)

print('Humano, estou lançando um desafio! Adivinhe o número inteiro que eu escolhi de 0 a 10!')
print('')
numero_maquina = randint(1, 10)

numero_humano = int(input('Digite o número: '))
tentativa = 0

while numero_humano != numero_maquina:
    numero_humano = int(input('Você errou, mas vou te dar mais uma chance! Digite outro número: '))
    tentativa += 1
print('')

if tentativa >= 0:
    if tentativa == 0:
        print(f'Uau! Eu escolhi o número {numero_maquina}. Caramba! Você acertou de primeira. Tem certeza que não é uma máquina que nem eu? ')

    else:
        print(f'Ufa, finalmente você acertou! Caramba, precisou de {tentativa+1} tentativas! Um humano nunca ganhará de uma máquina!')
print('')
