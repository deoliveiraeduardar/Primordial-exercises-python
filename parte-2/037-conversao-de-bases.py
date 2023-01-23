print('---'*15)
print('INTEGER CONVERSION TO BINARY, OCTAL OR HEXADECIMAL BASE')
print('---'*15)

number = int(input('\033[1mEnter the number you want to convert: \033[m'))
print('')


print('''Knowing the following information:
Conversion to binary: type 1
Conversion to octal: type 2
Conversion to hexadecimal: type 3''')
conversion = int(input('\033[1mWrite the number that indicates the desired base: \033[m'))
print('')

if conversion == 1:
    print(f'The number {number} converted to BINARY is equal to {bin(number)[2:]}.')

elif conversion == 2:
    print(f'The number {number} converted to OCTAL is equal to {oct(number)[2:]}.')

elif conversion == 3:
    print(f'The number {number} converted to HEXADECIMAL is equal to {hex(number)[2:]}.')

else:
    print('You have not entered a matching number. Try again.')

cc = {
    'binario': '1',
    'octal': '2',
    'hexadecimal': '3'
}
