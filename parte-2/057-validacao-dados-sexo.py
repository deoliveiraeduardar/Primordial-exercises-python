import time
print('----'*5, 'VALIDAÇÃO DE DADOS: SEXO', '----'*5)
print('')

# .upper()[0] para pegar só a primeira letra com fatiamento
sexo = str(input(('Digite F para feminino ou M para masculino: ')))
sexo = sexo.upper()
print(f'Você digitou {sexo}')
print('Processando')
time.sleep(2)
print('')

# Essa forma de while está incorreto, pois com isso digo: enquanto sexo for diferente de F
# e for diferente de M, rodar tudo abaixo. Ficará em eterno loop, pois F sempre será diferente
# de M e M sempre será diferente de F.
# while sexo != 'F' and sexo != 'M':


# Usar while dessa forma, pois com isso digo: enquanto 'MF' não estiver em sexo, rodar o código.
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: '))
    sexo = sexo.upper()

print(f'Sexo {sexo} registrado com sucesso.')
