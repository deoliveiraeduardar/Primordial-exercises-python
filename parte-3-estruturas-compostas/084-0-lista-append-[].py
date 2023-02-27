lista_teste = list()
lista_teste.append('Gustavo')
lista_teste.append(40)
print(f'Print da lista teste: {lista_teste}')
print('')

lista_galera = list()
print('')

lista_galera.append(lista_teste)
print('Após galera.append(lista_teste):')
print(f'Print da lista_galera: {lista_galera}')
print('')

print('Agora vou mudar a lista_teste[0] = Eduarda e lista_teste[1] = 26:')
lista_teste[0] = 'Eduarda'
lista_teste[1] = 26
lista_galera.append(lista_teste)
print('')

# A resposta fica dupla, pois dei dois append (lista-teste).
# Criei uma ligação entre as duas estrutuas.
# Isso significa que, automaticamete, muda a lista_galera e a lista_teste também
print(f'Print da lista_galera: {lista_galera}')
