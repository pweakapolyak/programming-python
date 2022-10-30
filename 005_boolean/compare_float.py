import math

a = 0.1 + 0.2
b = 0.3000005325236346346

# print(a)
# print(b)
# print(a == b) - wrong

# d = abs(a-b)
# eps = 1e-6
#
# print(d <= eps)

print(math.isclose(a, b, abs_tol=1e-6))