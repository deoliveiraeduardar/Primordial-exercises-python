print('SAIBA TODOS OS NÚMERO PARES DO INTERVALO')
print('----'*20)
print('')

i = int(input('Digite o número de início do intervalo: '))
f = int(input('Digite o número de final do intervalo: '))

if f > i:
    for d in range (i, f+1):
        resto = d % 2
        if resto == 0:
            print(d)
elif f < i:
    for d in range (i-1, f+1, -1):
        resto = d % 2
        if resto == 0:
            print(d)
print('FIM')