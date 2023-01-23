#print('SAIBA A SOMA DOS ÍMPARES MÚLTIPLOS DE 3 NO INTERVALO SELECIONADO POR VOCÊ')
print('---'*30)
print('')

i = int(input('Digite o número de início do intervalo: '))
f = int(input('Digite o número de final do intervalo: '))


soma = 0
#quantos números tem
contador = 0

if i < f:
    for d in range(i,f+1):
        resto2 = d % 2
        resto3 = d % 3
        if resto2 != 0 and resto3 == 0:
            print(d)
            soma += d
            contador += 1
else:
    for d in range(f,i+1):
        resto2 = d % 2
        resto3 = d % 3
        if resto2 != 0 and resto3 == 0:
            print(d)
            soma += d
            contador += 1
print(f'Nesse intervalo existem {contador} números múltiplos de três.\nA soma deles é: {soma}')
