

# n = int(input('Enter num: '))
# for i in range(n):
#     print(i)

# i = 0
# while i < n:
#     print(i)
#     i += 1


# for i in range(5, 101, 5):
#     print(i)

count = 0
for i in range(10):
    for j in range(10):
        print(10*i + j, end='\t')
        count += 1
    print()

print('Num of iterations', count)