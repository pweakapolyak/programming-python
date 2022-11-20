

# 5! = 1 * 2 * 3 * 4 * 5

n = 5
factorial = 1
for i in range(n):
    factorial *= i+1

print('Factorial: ', factorial)



def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print('Recursion factorial', factorial(5))