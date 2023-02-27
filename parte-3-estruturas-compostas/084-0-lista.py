dados = ['Pedro', 25]
print(dados)

pessoas = list()
# Peguei dados, coloquei uma cópia dos dados e vou dar um append
# Agora tenho uma lista (pessoas). E dentro dessa lista tenho outra lista (dados)
pessoas.append(dados[:])
