print('===='*21)
print('ANALISANDO INFORMAÇÕES SOBRE UMA LETRA ESPECÍFICA NA FRASE QUE VOCÊ DIGITAR')
print('===='*21)

#Digitar a frase
#colocar em minuscul
#Digitar o caracter que quer buscar
#colocar em minuscul
#Converter em caracteres índices
#Analisar quants vezes a letra a aparece na tela

#Analisar em que posição ela aparece primeiro.A
#Analisar em que poisção ela aparece por último.

frase = str(input('Digite a frase que você quer analisar: ')).lower()
letra = str(input('Digite a letra que você quer ter analisar na respectiva frase: ')).lower()
print('')


#Quanas vezes a letra aparece
print(f'A frase "{frase}" contém {frase.count(letra)} letras "{letra}".')

#Em que posição aparece pela primeira vez, contantando os espaços e somando +1, pois no python começa com 0
print('A letra "{}" aparece pela primeira vez nessa frase na posição de número {}'.format(letra, frase.find(letra)+1))

#Em que posição aparece pela ultima vez
print(f'A letra "{letra}" aparece pela última vez na posição de número {frase.rfind(letra)+1}.')