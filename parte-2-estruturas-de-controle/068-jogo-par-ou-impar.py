import random
import time
import emoji

print('===='*8, 'VAMOS JOGAR PAR OU ÍMPAR!', '===='*8)
print('*Mas só vamos parar de jogar quando você perder, humano!')

while True:
    lista = []
    soma = 0
    contador = 0

    par_ou_impar = ' '
    humano_numero = 0

    # GERANDO LISTA
    print('------' * 13)
    for d in range(1, 10 + 1):
        lista.append(d)
    maquina_numero = random.choice(lista)
    humano_numero = int(input('\033[1mUm, dois, três e já! Digite um número de 0 a 10: \033[m'))

    while par_ou_impar not in 'PI':
        par_ou_impar = str(input('\033[1mLevando em conta P para par e I para ímpar. Digite a sua escolha: \033[m')).upper()

    soma = maquina_numero + humano_numero
    print('')
    time.sleep(1)

    print(emoji.emojize('Contando nossos dedos virtuais... :hand_with_fingers_splayed:'))
    print('')
    time.sleep(1)

    # SE A SOMA FOR PAR
    if soma % 2 == 0:
        print(f'A soma de {maquina_numero}+{humano_numero}= {soma}. É par!')
        print('')
        time.sleep(0.5)
        if par_ou_impar in 'P':
            print('Como você escolheu par, você ganhou! Parabéns, humano!')
            time.sleep(1)
            print('O nosso combinado é nós dois jogarmos até você perder.')
            time.sleep(1)
            print('Por favor, deixa eu treinar o meu algoritmo com você')
            print(emoji.emojize('Vamos lá de novo!:pleading_face:'))
            contador += 1
            time.sleep(3)

            print('')
        else:
            print('Como você escolheu ímpar, você perdeu!!')
            print(emoji.emojize('Nós, máquinas, vamos dominar o mundo! :smiling_face_with_sunglasses:'))
            contador += 1
            break

    # SE A SOMA FOR ÍMPAR
    elif soma % 2 != 0:
        print(f'A soma de {maquina_numero}+{humano_numero}= {soma}. É ímpar!')
        print('')
        time.sleep(0.5)
        if par_ou_impar in 'I':
            print('Como você escolheu ímpar, você ganhou! Parabéns, humano!')
            time.sleep(1)
            print('O nosso combinado é nós dois jogarmos até você perder.')
            time.sleep(1)
            print('Por favor, deixa eu treinar o meu algoritmo com você')
            print(emoji.emojize('Vamos lá de novo!:pleading_face:'))
            contador += 1
            time.sleep(3)
        else:
            print('Como você escolheu par, você perdeu!!')
            print(emoji.emojize('Nós, máquinas, vamos dominar o mundo!:smiling_face_with_sunglasses:'))
            contador += 1
            break
print(f'Nos jogamos {contador} vezes! Foi divertido. Até mais!')
