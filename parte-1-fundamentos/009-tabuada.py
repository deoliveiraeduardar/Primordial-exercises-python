print('========='*5)
print('TABUADA')
print('========='*5)
n = int(input('Digite o numerador da sua tabuada: '))
print('')

for a in range(1, 10):
    r = a*n
    print('{} x {}= {}'.format(n, a, r))
    a = a+1
