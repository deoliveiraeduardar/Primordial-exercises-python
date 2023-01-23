import random
from emoji import emojize

print('---'*15)
print('JOKENPÔ COM UMA MÁQUINA')
print('---'*15)
print('')

lista = ['pedra', 'papel', 'tesoura']
maquina = random.choice(lista)
print(f'A máquina escolheu {maquina}')

humano = str(input('Você quer pedra, papel ou tesoura? ')).lower()

if maquina == humano:
    print(emojize(f'Xii, deu empate! Eu também escolhi {maquina}. Sinta-se honrado em empatar com uma máquina! :smiling_face_with_sunglasses:'))

if maquina == 'pedra' and humano == 'tesoura':
    print(emojize(f'Eu escolhi {maquina}. Eu ganhei! As máquinas irão dominar o mundo, muahahaha! :smiling_face_with_sunglasses:'))

if maquina == 'pedra' and humano == 'papel':
    print(emojize(f'Eu escolhi {maquina}. Vou programar um e-mail para o dev que me fez! Preciso de um código melhor! :loudly_crying_face:'))

if maquina == 'tesoura' and humano == 'papel':
    print(emojize(f'Eu escolhi {maquina}. Eu ganhei! As máquinas irão dominar o mundo, muahahaha! :smiling_face_with_sunglasses:'))

if maquina == 'tesoura' and humano == 'pedra':
    print(emojize(f'Eu escolhi {maquina}. Eu perdi para um humano! Vou programar um e-mail para o dev que me fez! Preciso de um código melhor! :loudly_crying_face:'))


if maquina == 'papel' and humano == 'tesoura':
    print(emojize(f'Eu escolhi {maquina}. Eu perdi para um humano! Que absurdo! Preciso de um código melhor!'))

if maquina == 'papel' and humano == 'pedra':
    print(emojize(f'Eu escolhi {maquina}. Eu perdi para um humano! Que vergonha! :loudly_crying_face:'))