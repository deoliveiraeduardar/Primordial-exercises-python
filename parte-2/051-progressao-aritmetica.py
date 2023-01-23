print('---'*16)
print('SABENDO INFORMAÇÕES DE UMA PA')
print('---'*16)
print('')

a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
termo = int(input('Digite até qual termo você quer calcular: '))
print('')

for d in range(1,termo+1):
    calculo = a1 + (d - 1) * r
    #print(f'Termo {d}: valor de {calculo}')
    print('{} '.format(calculo), end='↠ ')
