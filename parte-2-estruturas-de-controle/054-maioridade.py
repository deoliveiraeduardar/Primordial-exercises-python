print('-----'*15)
print('SAIBA SOBRE A MAIORIDADE')
print('-----'*15)

pessoas = int(input('Digite o número de pessoas que você quer analisar? '))
maiorcontador = 0
menorcontador = 0

for d in range(1, pessoas + 1):
    ano = int(input(f'Digite o ano de nascimento da {d}ª pessoa: '))
    if ano <= 2005:
        maiorcontador += 1
    else:
        menorcontador += 1

print('')
print(f'Há {maiorcontador} pessoas que atingiram a maioridade e {menorcontador} pessoas que são menores de idade.')