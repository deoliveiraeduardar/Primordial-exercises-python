print('SAIBA SE É UM TRIÂNGULO OU NÃO')
print('')

r1 = float(input('Digite o número da primeira reta: '))
r2 = float(input('Digite o número da segunda reta: '))
r3 = float(input('Digite o número da terceira reta: '))
print('')

if (r1 + r2 > r3) and (r2 + r3 > r1) and (r3 + r1 > r2):
    print('É um triângulo!')

else:
    print('Não é um triângulo!')

if r1 == r2 == r3:
    print('É um triângulo equilátero, pois tem 3 lados iguis')

if (r1 == r2) or (r1 == r3) or (r3 == r2):
    print('É um triângulo isósceles, pois tem 2 lados iguais.')

if (r1 != r2) and (r2 != r3) and (r3 != r2) and (r3 != r1):
    print ('É um triânguo escaleno, pois tem 3 lados diferentes.')