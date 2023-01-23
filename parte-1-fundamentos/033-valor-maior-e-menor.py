print('----'*15)
print('DIGITE 3 NÚMEROS E SAIBA QUAL É O MENOR E O MAIOR')
print('----'*15)

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))
print('')

if (n1 > n2) and (n1 > n3):
    if (n2 > n3):
        print(f' {n1}, {n2}, {n3}')
    else:
        print(f'A ordem crescente é: {n1}, {n3}, {n2}')

if (n2 > n1) and (n2 > n3):
    if (n1 > n3):
        print(f' {n2}, {n1}, {n3}')
    else:
        print(f'A ordem crescente é: {n2}, {n3}, {n1}')

if (n3 > n1) and (n3 > n2):
    if (n1 > n2):
        print(f' {n3}, {n1}, {n2}')
    else:
        print(f'A ordem crescente é: {n3}, {n2}, {n1}')