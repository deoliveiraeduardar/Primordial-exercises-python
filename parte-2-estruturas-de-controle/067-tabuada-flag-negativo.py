
import time
entrada_tabuada = 0
numero = 0

while True:
    print('====='*15)
    print('*Caso queira parar, é só digitar um número negativo.')
    entrada_tabuada = int(input('\033[1mDigite o número que você quer ver a tabuada: \033[m'))
    if entrada_tabuada < 0:
        print('Finalizando o algoritmo...')
        time.sleep(1)
        print('Até logo!')
        break
    elif entrada_tabuada == 0:
        print(f'   \033[1mHumano, acho que essa tabuada você sabe decor!\033[m')
        print(f'   \033[1mMas, tudo bem, se é isso que você quer... aí vai\033[m')
        time.sleep(3)
        print('')
    for d in range(1, 10+1):
        print(f'{entrada_tabuada} x ' f'{d}= ' f'{entrada_tabuada * d}')
    time.sleep(1)
    print('')
