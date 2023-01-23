print('===='*21)
print('ANÁLISE SE CONTÉM UMA PALAVRA ESPECÍFICA NA FRASE QUE VOCÊ DIGITAR"')
print('===='*21)


#Inserir o nome da cidade
#converter tudo em minúsculo
#Gerar uma lista do nome
#Analisar toda a frase
#Usar if

frase = str(input('Digite a frase completa: '))
pesquisa = str(input('Digite o nome que você quer buscar nessa frase: '))
print('')

frase = frase.lower()
frase = frase.split()

pesquisa = pesquisa.lower()

if pesquisa in frase:
    print(f'Sim, a palavra {pesquisa} está na frase que você digitou')

else:
    print('A palavra {} não está na frase que você digitou'.format(pesquisa))