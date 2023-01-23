import time

print('CÁLCULO DA MÉDIA GERAL DA SUA NOTA VALENDO PESO')

time.sleep(1)
print('Para isso, vou precisar que você insira a sua nota e o peso')
print('')

time.sleep(1)
t = int(input('Digite quantas notas você irá inserir: '))
time.sleep(1)
print(f'Ok! Vamos calcular sua média com {t} notas')
print('')

if t == 1:
    n1 = float(input('Digite a sua primeira nota: '))
    print('')
    print('Ué, por que você está utilizando o meu cérebro? Use o seu!')

if t >= 2:
    n1 = float(input('Digite a sua primeira nota: '))
    p1 = float(input('Digite o peso que ela tem: '))
    print('')

    n2 = float(input('Digite a sua segunda nota: '))
    p2 = float(input('Digite o peso que ela tem: '))
    print('')

if t >= 3:
    n3 = float(input('Digite a sua terceira nota: '))
    p3 = float(input('Digite o peso que ela tem: '))
    print('')

if t >= 4:
    n4 = float(input('Digite a sua quarta nota: '))
    p4 = float(input('Digite o peso que ela tem: '))
    print('')

if t >= 5:
    n5 = float(input('Digite a sua quinta nota: '))
    p5 = float(input('Digite o peso que ela tem: '))
    print('')

if t >= 6:
    n6 = float(input('Digite a sua sexta nota: '))
    p6 = float(input('Digite o peso que ela tem: '))
    print('')

if t >= 7:
    n7 = float(input('Digite a sua sétima nota: '))
    p7 = float(input('Digite o peso que ela tem: '))
    print('')

if t >= 8:
    n8 = float(input('Digite a sua oitava nota: '))
    p8 = float(input('Digite o peso que ela tem: '))
    print('')

if t == 1:
    print('A sua média é exatamente o valor que você digitou: {}'.format(n1))

if t == 2:
    m = ((n1 * p1) + (n2 * p2)) / (p1 + p2)
    if m >= 10:
        m = 10
        print(f'A sua média final é: {m}')
    else:
        print(f'A sua média final é: {m}')


if t == 3:
    m = ((n1 * p1) + (n2 * p2)) + (n3 * p3) / (p1 + p2 + p3)
    if m >= 10:
        m = 10
        print(f'A sua média final é: {m}')
    else:
        print(f'A sua média final é: {m}')

if t == 4:
    m = ((n1 * p1)+(n2 * p2))+(n3 * p3)+(n4 * p4)/(p1 + p2 + p3 + p4)
    if m >= 10:
        m = 10
        print(f'A sua média final é: {m}')
    else:
        print(f'A sua média final é: {m}')

if t == 5:
    m = ((n1 * p1)+(n2 * p2))+(n3 * p3)+(n4 * p4)+(n5 * p5)/(p1 + p2 + p3 + p4+p5)
    if m >= 10:
        m = 10
        print(f'A sua média final é: {m}')
    else:
        print(f'A sua média final é: {m}')

if t == 6:
    m = ((n1 * p1)+(n2 * p2))+(n3 * p3)+(n4 * p4)+(n5 * p5)+(n6 * p6)/(p1 + p2 + p3 + p4+p5+p6)
    if m >= 10:
        m = 10
        print(f'A sua média final é: {m}')
    else:
        print(f'A sua média final é: {m}')

if t == 7:
    m = ((n1 * p1)+(n2 * p2))+(n3 * p3)+(n4 * p4)+(n5 * p5)+(n6 * p6)+(n7*n7)/(p1 + p2 + p3 + p4 + p5 + p6 + p7)
    if m >= 10:
        m = 10
        print(f'A sua média final é: {m}')
    else:
        print(f'A sua média final é: {m}')

if t == 7:
    m = ((n1 * p1) + (n2 * p2)) + (n3 * p3) + (n4 * p4) + (n5 * p5) + (n6 * p6) + (n7 * p7) + (n8*p8) / (p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8)
    if m >= 10:
        m = 10
        print(f'A sua média final é: {m}')
    else:
        print(f'A sua média final é: {m}')

if t == 8:
    m = ((n1 * p1) + (n2 * p2)) + (n3 * p3) + (n4 * p4) + (n5 * p5) + (n6 * p6) + (n7 * p7) + (n8 * p8) / (
                    p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8)
    if m >= 10:
        m = 10
        print(f'A sua média final é: {m}')
    else:
        print(f'A sua média final é: {m}')