import random
print('---'*25)
print('SORTEANDO A ORDEM DE APRESENTAÇÃO')
print('---'*25)

a1 = str(input('Digite o nome do 1º aluno: '))
a2 = str(input('Digite o nome do 2º aluno: '))
a3 = str(input('Digite o nome do 3º aluno: '))
a4 = str(input('Digite o nome do 4º aluno: '))
print('')

lista = [a1, a2, a3, a4]
random.shuffle(lista)
print('A ordem de apresentação será {}'.format(lista))