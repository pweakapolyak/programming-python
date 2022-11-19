import time

def super_slow_function(number):
    time.sleep(1.5)
    return number / 5 * 2e-5

cache = {}

def cache_function(number):
    if number in cache:
        return cache[number]
    else:
        result = super_slow_function(number)
        cache[number] = result
        return result

print('Call 1', cache_function(5))
print('Call 2', cache_function(4))
print('Call 3', cache_function(5))
print('Call 4', cache_function(4))
print('Call 5', cache_function(5))