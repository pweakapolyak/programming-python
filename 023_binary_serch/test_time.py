import time
from slow import binary_search_1
from fast import binary_search_2

big_list = []

for i in range(0, 50_000_000):
    big_list.append(i)

start = time.time()
print(50_000_000-1 in big_list)
end = time.time()
print('In list', end-start)

start = time.time()
print(binary_search_1(big_list, 50_000_000-1))
end = time.time()
print('binary search 1', end-start)

start = time.time()
print(binary_search_2(big_list, 50_000_000-1, 0, len(big_list)-1))
end = time.time()
print('binary search 2', end-start)