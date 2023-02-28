num = [[], []]
valor = 0

for d in range(1, 8):
    valor = int(input(f'Digite o {d}º valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
        print(f'Printando lista num APÓS INSERIR PAR: {num}')
    else:
        num[1].append(valor)
        print(f'Printando lista num APÓS INSERIR ÍMPAR: {num}')

num[0].sort()
num[1].sort()
print(f'Valores pares em ordem: {num[0]}')
print(f'Valores ímpares em ordm: {num[1]}')
