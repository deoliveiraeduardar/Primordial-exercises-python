import time
print('''   Criar um programa que lê vários números inteiros. O programa deve
parar quando o usuário digitar 999 (flag). No final deve mostrar
quantos números foram digitados e a soma deles, desconsiderando o flag.''')
print('====='*15)
time.sleep(1)

contador = 0
soma = 0
n = 0

while n != 999:
    time.sleep(0.2)
    n = int(input('Caso queira parar, é só digitar 999.\nDigite um número: '))
    print('')

    if n == 999:
        print('Parando o processo...')
        break

    contador += 1
    soma += n
print(f'\033[1mVocê digitou {contador} números. A soma deles é {soma}.\033[m')
