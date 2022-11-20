import time

# fib(n) = fib(n-1) + fib(n-2)

def fibonacci_loop(n):
    f_prev_prev = 0
    f_prev = 1

    if n == 1:
        return f_prev_prev
    elif n == 2:
        return f_prev

    f_n = 0
    for i in range(n-2):
        f_n = f_prev_prev + f_prev
        f_prev_prev = f_prev
        f_prev = f_n

    return f_n

num_calls = 0
cache = {}
def fibonacci_recursion(n):
    global num_calls
    num_calls += 1

    if n in cache:
        return cache[n]

    if n == 1:
        return 0
    elif n == 2:
        return 1

    result = fibonacci_recursion(n-1) + fibonacci_recursion(n-2)
    cache[n] = result

    return result


start = time.time()
print('Loop fib: ', fibonacci_loop(35))
end = time.time()
print('Loop: ', end-start)


start = time.time()
print('Recursion fib: ', fibonacci_recursion(35))
print('Num of calls: ', num_calls)
end = time.time()
print('Recursion: ', end-start)