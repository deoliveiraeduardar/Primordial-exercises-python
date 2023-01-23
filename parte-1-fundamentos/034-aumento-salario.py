print('SAIBA QUANTO O SALÁRIO VAI AUMENTAR')
print('----'*15)
print('*O aumento será de 10% para salários superiores a R$ 1250 e \nde 15% para o restante')
print('')

s = float(input('Digite o salário: '))
print('')

if s > 1250:
    ns = (110*s)/100
    print(f'Com aumento de 10% o salário será de R$ {ns}')

if s <= 1250:
    nss = (115*s) / 100
    print(f'Com aumento de 15% o salário será de R$ {nss}')