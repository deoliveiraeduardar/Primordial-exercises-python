print('Enter as many numbers as you want and know the total sum between them')
print('----'*20)
print('*If you want to stop the sum, type 999')
print('')

n = count = add = 0
n = float(input('Type the number: '))

while n != 999:
    add += n
    count += 1
    n = float(input('Type the number: '))

print(f'You entered {count} numbers. Adding them all up, the total is {add}')
print('END')
