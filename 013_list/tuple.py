


t1 = (1,2,3)
t2 = ("Hello", False)

print('T1: ', t1)
print('T2: ', t2)
print('Length T1: ', len(t1))
print('Length T2: ', len(t2))

print(t1+t2)

for element in t1+t2:
    print('Element: ', element)


# t1[0] = 5 - FAILED

def f():
    return (1, 2, 3)


print(f())

a, b, c = f()
print('a=', a)
print('b=', b)
print('c=', c)