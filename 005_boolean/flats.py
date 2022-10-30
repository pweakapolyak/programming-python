

price = 13_500_000
num_rooms = 2
distance_to_subway = 350

filter_1 = price <= 15_000_000 and num_rooms >= 2
filter_2 = (price >= 11_000_000 and price <= 22_000_000) or (distance_to_subway < 200)
filter_3 = not (num_rooms == 2)

print(filter_1)
print(filter_2)
print(filter_3)