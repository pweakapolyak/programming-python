import time

list = []
for i in range(0, 20_000_000):
    list.append(i)


start = time.time()
var1 = list[20_000_000-1]
end = time.time()

print('Get by index in list : ', end-start)

start = time.time()
var2 = 20_000_001 in list
end = time.time()

print('Find in list : ', end-start)




