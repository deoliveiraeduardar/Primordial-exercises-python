lista = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON',
         'CURSO', 'SOBRE', 'ESTUDAR', 'PRATICAR', 'TRABALHAR',
         'MERCADO', 'PROGRAMADOR', 'FUTURO')


for p in lista:
    print(f'\nNa palavra {p} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end=' ')

