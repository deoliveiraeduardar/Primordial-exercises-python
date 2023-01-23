import time

print('EXCESSO DE VELOCIDADE: DESCUBRA O VALOR DA SUA MULTA')
print('-----'*16)
print('*É necessário saber a velocidade permitida no trecho em que você ultrapassou')
print('')
time.sleep(3)

vrodo = int(input('Digite a velocidade permitida na rodovia: '))
vc = float(input('Digite a velocidade que você estava dirigindo: '))
print('')

#1. calculando o quanto a velocidade do condutor foi
#percentualmente maior que a permitida
calculo = ((vc*100)/vrodo)-100
#print(calculo)

if (calculo > 0) and (calculo <= 20):
    print('Você cometeu uma infração média e terá 4 pontos na carteira.')
    print('A sua penalidade será uma multa de R$ 130,16')

if (calculo > 20) and (calculo <= 50):
    print('Você cometeu uma infração grave e terá 5 pontos na carteira.')
    print ('A sua penalidade será uma multa de R$ 195,23')

if calculo > 50:
    print('Você cometeu uma infração gravíssima e terá 7 pontos na carteira.')
    print('Você terá algumas penalidades:')
    print('   - Multa (três vezes).')
    print('   - Suspensão do direito de dirigir.')


if calculo == 0:
    print('Parabéns! Você não foi multado!')