print('===='*19)
print('VERIFICANDO SE A CIDADE COMEÇA COM O NOME "SANTO"')
print('===='*19)

#Inserir o nome da cidade
#converter tudo em minúsculo
#Gerar uma lista do nome
#Analisar somente a primeira palavra

#Usar if para a primira palavra

nome = str(input('Digite o nome da cidade que você quer analisar: '))
print('')
nome = nome.lower()

lista = nome.split()
item = lista[0]

if item =='santo':
    print('A cidade contém o nome "santo" na primeira palavra!')

else:
    print('A cidade não contém o nome "santo" na primeira palavra!')