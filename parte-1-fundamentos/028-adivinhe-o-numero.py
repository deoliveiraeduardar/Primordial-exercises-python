import random

print('----'*10)
print('TENTE DESCOBRIR QUE NÚMERO EU PENSEI DE 0 A 5')
print('----'*10)

#Programa sorteando
lista = [0, 1, 2, 3, 4, 5]
escolhido = random.choice(lista)

#Pessoa digitando
n = int(input('Digite o número que você acha que eu pensei: '))
print('')

if n == escolhido:
    print ('Uauu! Você tinha 16% de chance e conseguiu acertar! Eu realmente escolhi o número {}'.format(n))
    print ('Parabéns!')

else:
    print(f'Poxa, que chato! Você não acertou. Eu escolhi o número {escolhido}')
    print('Fica pra próxima! É melhor você treinar!')

