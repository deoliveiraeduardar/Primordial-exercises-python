import time
from math import factorial

print('----'*5, 'DESCUBRA O FATORIAL COM WHILE', '----'*5)

numero = int(input('Digite o número: '))
resultado = 1
count = 1

while count <= numero:
    resultado *= count
    count += 1
print(f'O fatorial de {numero} é {resultado}.')

time.sleep(0.5)

print('')
print('')
print('====='*15)
print('----'*5, 'DESCUBRA O FATORIAL COM FOR', '----'*5)
time.sleep(1)

n = int(input('Digite o número: '))
calculo = numero

for d in range(1, n):
    calculo *= d
print(f'O fatorial de {n} é {calculo}.')

print('')
print('')
print('====='*15)
print('----'*5, 'DESCUBRA O FATORIAL COM BIBLIOTECA MATH', '----'*5)
time.sleep(1)

n = int(input('Digite o número: '))
f = factorial(n)
print(f'O fatorial de {n} é {f}.')

print('')
print('\033[1mFIM\033[m')
