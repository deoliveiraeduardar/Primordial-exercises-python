print('CONTAGEM REGRESSIVA')
print('---'*15)
import time

i = int(input('Digite a partir de quantos segundos quer fazer a contagem regressiva: '))

for d in range (i,0-1,-1):
    print(d)
    time.sleep(1)
print('FIM')