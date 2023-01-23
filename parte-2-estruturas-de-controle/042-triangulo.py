print('---'*14)
print('SAIBA INFORMAÇÕES SOBRE TRIÂNGULOS')
print('---'*14)

a = float(input('Digite o comprimento da primeira reta: '))
b = float(input('Digite o comprimento da segunda reta: '))
c = float(input('Digite o comprimento da terceira reta: '))
print('')

if ((a + b) > c) and ((a + c)> b) and ((b + c) > a):
    print('As retas formam um triângulo.')
    if a == b == c:
        print('Elas formam um triângulo equilátero, pois os três tamanhos são iguais.')

    elif a != b != c:
        print('Elas formam um triângulo escaleno, pois há três tamanhos diferentes.')

    elif (a == b != c) or (a == c != b) or (b == c != a):
        print('Como há duas retas iguais, o triângulo é isósceles.')

else:
    print('As retas não formam um triângulo. Tente outros comprimentos de reta.')
