import math
print('==='*35)
print('CALCULE QUANTOS LITROS DE TINTA VOCÊ PRECISA PARA PINTAR UMA DETERMINADA ÁREA')
print('==='*35)

l = float(input('Digite a largura em metros: '))
a = float(input('Digite a altura em metros: '))
area = l*a
litros = area/2
print('')

print('Como 1 litro de tinta pinta uma área de 2m², você precisará de {} litros'.format(litros))