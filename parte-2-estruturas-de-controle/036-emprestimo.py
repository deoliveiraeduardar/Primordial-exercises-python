print('---'*15)
print('APROVAÇÃO DE EMPRÉSTIMO BANCÁRIO')
print('---'*15)

casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o seu salário mensal: '))
tempo = int(input('Digite em quantos anos quer pagar: '))*12
print(tempo)
print('')

prestacao = casa/tempo
# print(f'O valor da prestação mensal será de R$ {prestacao:.2f}')
porcentagem = (prestacao*100)/salario
# print(f'O valor da porcentagem da prestação em relação ao salário é de {porcentagem:.2f}')

if porcentagem > 30:
    print('O empréstimo foi {}negado{}, pois a prestação equivale a {:.2f}% do seu salário'.format('\033[31m', '\033[m', porcentagem))
else:
    print(f'O seu empréstimo foi \033[42maprovado\033[42m, pois a prestação da casa equivale a {porcentagem:.2f}% do seu salário.')
