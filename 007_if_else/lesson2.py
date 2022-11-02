


age = int(input('Enter age:'))

if age < 0:
    print('Input incorrect')
    exit(-1)


if age < 10:
    print('Child')
elif age < 20:
    print('Teen')
elif age < 30:
    print('Middle')
elif age < 50:
    print('Mature')
else:
    print('Old')


