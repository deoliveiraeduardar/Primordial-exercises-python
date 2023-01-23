print('===='*19)
print('ESCOLHA UM NÚMERO DE 0 A 9999 E SAIBA OS DÍGITOS SEPARADOS')
print('===='*19)

num = int(input('Digite um número de 0 a 9999: '))
n = str(num)
nn = len(n)

if nn == 4:
    print(f'Unidade: {n[3]}')
    print(f'Dezena: {n[2]}')
    print(f'Centena: {n[1]}')
    print(f'Milhar: {n[0]}')

if nn == 3:
    print(f'Unidade: {n[2]}')
    print(f'Dezena: {n[1]}')
    print(f'Centena: {n[0]}')

if nn == 2:
    print(f'Unidade: {n[1]}')
    print(f'Dezena: {n[0]}')

if nn == 1:
    print(f'Unidade: {n[0]}')

elif nn>=5:
    print('Opa, você não digitou um número de 0 a 9999!')
    print('Terá de refazer o procedimento.')