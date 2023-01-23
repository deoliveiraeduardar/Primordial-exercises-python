print('\033[1mCHALLENGE: GENERATE A PROGRAM THAT DISPLAYS N ELEMENTS OF THE FIBONACCI SEQUENCEE\033[m')
print('---'*28)
print('')

n = int(input('Enter up to which element number you want to see: '))
calculation = 0
print('')

t1 = 0
t2 = 1

print(f'{t1} → {t2}', end='')
count = 3

while count <= n:
    t3 = t1 + t2
    print(f' → {t3}', end='')
    count += 1
    t1 = t2
    t2 = t3

print(' →→ END')
