import math
print('---'*25)
print('SAIBA O COMPRIMENTO DA HIPOTENUSA')
print('---'*25)
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
h = math.hypot(co, ca)
print(f'O valor da hipotenusa é {h}')