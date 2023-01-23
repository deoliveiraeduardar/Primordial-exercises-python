print('---'*20)
print('SABENDO INFORMAÇÕES DA FRASE')
print('---'*20)

a = str(input('Digite a frase completa: '))
print('Em maiúsculo fica: {}'.format(a.upper()))
print('Em minúsculo fica: {}'.format(a.lower()))
print('Com a inicial e cada palavra em maiúsculo fica: {}'.format(a.title()))
print('')
print('A frase, contando os espaços em branco, tem {} caracteres'.format(len(a)))


#contando caracteres sem espaços
asemespaco = len(a.replace(' ',''))
print('A frase, sem contar os espaços, tem {} caracteres'.format(asemespaco))



