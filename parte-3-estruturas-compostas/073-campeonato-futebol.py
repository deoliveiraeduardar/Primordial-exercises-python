times = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Atlético', 'Paranaense', 'Atlético', 'Fortaleza', 'São Paulo', 'América FC', 'Botafogo', 'Santos', 'Goiás', 'Red Bull', 'Coritiba', 'Cuiabá', 'Ceará', 'Atlético', 'Avaí', 'Juventude')

print(f'Cinco primeiros colocados: {times[0:6]}')
print(f'Quatro últimos colocados: {times[16:20]}')
print(f'Times em ordem alfabética: {sorted(times)}')
print('')

# PEGANDO O CHAPECOENSE
indice = times.index('Fortaleza')
print(f'Fortaleza está na posição: {indice}')


