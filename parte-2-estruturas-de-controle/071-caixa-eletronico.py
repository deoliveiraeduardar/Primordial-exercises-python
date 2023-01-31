import time
print('==='*10, 'CAIXA ELETRÔNICO', '==='*10)

cedulas = [50, 20, 10, 1]
ja_sacado = ' '

sacar = int(input('Digite o valor que você quer sacar: '))
print('Você vai receber:')

for cedula in cedulas:
    divisao_inteira = sacar // cedula
    resto = sacar % cedula
    if ja_sacado != 0:
        sacar = resto
    ja_sacado = (divisao_inteira * cedula) - sacar
    print(f'\033[1m   {divisao_inteira} cédulas de R$ {cedula}\033[m ')
    time.sleep(1)

print('')
print('Finalizando o caixa eletrônico... \nAté mais!')
