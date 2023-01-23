print('-----'*15)
print('É UM PALÍNDROMO?')
print('-----'*15)

# CAPTANDO A FRASE DE ENTRADA A SER ANALISADA
# upper: maiusculo e slplit: separar
entrada = str(input('Digite a frase ou palavra sem acentos: ')).upper().split()

# join: juntar tudo em uma unica palavra
entrada = ''.join(entrada)
inverso = ''
print('')

# DESMONTANDO E FAZENDO A PALAVRA INVERSA
for letra in range(len(entrada) - 1, - 1, -1):
    inverso += entrada[letra]
    # Inverso será a entrada reformulada com o for [letra]

print(f'O inverso do que você digitou é: {inverso}.')

if inverso == entrada:
    print('\033[1mUau! Temos um palíndromo!\033[m')
else:
    print('\033[1mEntão, não temos um palíndromo. Que pena!\033[m')
