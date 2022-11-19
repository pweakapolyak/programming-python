import time

list = []
set = set()
for i in range(0, 20_000_000):
    list.append(i)
    set.add(i)


start = time.time()
var1 = 20_000_001 in list
end = time.time()

print('Find in list : ', end-start)

start = time.time()
var1 = 20_000_001 in set
end = time.time()

print('Find in set : ', end-start)




