import math
print('*****'*20)
print('CALCULANDO INFORMAÇÕES SOBRE O TRIÂNGULO')
print('*****'*20)

a = float(input('Digite o valor do ângulo: '))
graus = str(input('Esse ângulo está em radianos? Digite 1 para sim ou 2 para não: '))
print('')

if graus == '2':
    a = math.radians(a)
else:
    a = a

s = math.asin(a)
c = math.acos(a)
t = math.atan(a)
print(f'O seno é de {s:.3f} radianos')
print(f'O cosseno é de {c:.3f} radianos')
print(f'A tangente é de {t:.3f} radianos')
