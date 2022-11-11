

a = 1
b = 2

print('Before function call: ')
print('Global a: ', a)
print('Global b: ', b)

def f(x):
    a = 5
    z = 10
    print('\nIn function: ')
    print('Local a', a)
    print('Global b', b)

f(b)

print('\nAfter function call: ')
print('Global a: ', a)
print('Global b: ', b)
