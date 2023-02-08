lista = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'PRÁTICA',
         'CURSO', 'SOBRE', 'ESTUDAR', 'PRATICAR', 'TRABALHAR',
         'MERCADO', 'PROGRAMADOR', 'FUTURO')


for p in lista:
    print(f'\nNa palavra {p} temos ', end='')
    for letra in p:
        if letra.lower() in 'aãâáàeêéèiíîóôouúû':
            print(letra.lower(), end=' ')

