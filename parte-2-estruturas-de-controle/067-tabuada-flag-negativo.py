
import time
entrada_tabuada = 0
numero = 0

while True:
    print('====='*15)
    entrada_tabuada = int(input('Digite o número que você quer ver a tabuada: '))
    if entrada_tabuada < 0:
        print('Finalizando o algoritmo...')
        time.sleep(1)
        print('Até logo!')
        break
    elif entrada_tabuada == 0:
        print(f'   Humano, acho que essa tabuada você sabe decor!')
        print(f'   Mas, tudo bem, se é isso que você quer... aí vai')
        time.sleep(3)
        print('')
    for d in range(1, 10+1):
        print(f'{entrada_tabuada} x ' f'{d}= ' f'{entrada_tabuada * d}')
    time.sleep(1)
    print('')
