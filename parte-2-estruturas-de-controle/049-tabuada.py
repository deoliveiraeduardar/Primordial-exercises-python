print('---'*15)
print('TABUADA')
print('---'*15)

num = int(input('Digite o número da tabuada que você quer: '))

for d in range(0,10+1):
    multi = num*d
    print(f'{num} x {d}= {multi}')