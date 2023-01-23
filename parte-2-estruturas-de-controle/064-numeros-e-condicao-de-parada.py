print('Enter as many numbers as you want and know the total sum between them')
print('----'*20)
print('*If you want to stop the sum, type 999')
print('')

n = 0
count = 0
add = 0

while n != 999:
    n = float(input('Type the number: '))
    add += n
    count += 1

print(f'You entered {count-1} numbers. Adding them all up, the total is {add-999}')
print('FIM')
