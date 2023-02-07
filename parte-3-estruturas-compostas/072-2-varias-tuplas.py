a = (2, 5, 4)
b = (5, 8, 1, 2)

c = a + b
print(c)
print('Quantos índices tem c:', len(c))
print('Quantas vezes, em c, aparece o número 5: ', c.count(5))
print('Em qual posição(índice), em c, aparece o 8: ', c.index(8))
print('Em qual posição(índice), em c, aparece o 2: ', c.index(2))
print('Em qual posição(índice), em c, aparece o 2, a partir da posição 1: ', c.index(2, 1))