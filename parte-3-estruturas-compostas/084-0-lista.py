dados = ['Pedro', 25]
print(dados)

pessoas = list()
# Peguei dados, coloquei uma cópia dos dados e vou dar um append
# Agora tenho uma lista (pessoas). E dentro dessa lista tenho outra lista (dados)
pessoas.append(dados[:])

# Lista pessoas é composta por 0, 1 e 2 índices
pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]
print(pessoas)

print(f'Print no índice 0 e item 0 (pessoas[0][0]): {pessoas[0][0]})')
print(f'Print no índice 1 e item 1 (pessoas[1][1]): {pessoas[1][1]})')
print(f'Print no índice 2 e item 0 (pessoas[2][0]): {pessoas[2][0]})')
