print('-----'*15)
print('LER NÚMEROS INTEIROS E SOMAR OS PARES')
print('-----'*15)

s = 0
num = int(input('Digite quantos números você quer ler: '))
print('')

for d in range(1,num+1):
    n = int(input(f'Digite o {d}º número: '))
    resto2 = n % 2
    #print(f'O resto é : {resto2}')
    print('')

    if resto2 == 0:
        s += n
        # print(f'A soma é {s}')
print('A soma dos valores pares é: {}'.format(s))
