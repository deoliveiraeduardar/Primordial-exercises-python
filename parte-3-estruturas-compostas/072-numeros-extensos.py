from num2words import num2words

numero = int(input('Digite um número: '))
extenso= num2words(numero, lang='pt-br')
print(f'Número por extenso: {extenso}')

# Usuário, digite um número que você quer ver por extenso
# numero_usuario = int(input('Digite o número que você quer ver por extenso: '))
