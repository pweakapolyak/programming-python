hero_hp = 100
enemy_damage = 25

print('Hero hp: ', hero_hp)
print('Enemy damage: ', enemy_damage)

hero_hp = hero_hp - enemy_damage
print('Hero hp: ', hero_hp)

print( type(hero_hp) )
hero_hp = "test"
print( type(hero_hp) )
age_Anya = int(input('Возраст Ани: '))
age_Sasha = int(input('Возраст Саши: '))
print('возраст Ани: ', age_Anya)
print('возраст Саши: ', age_Sasha)
age_diff = age_Sasha - age_Anya
print('Саша старше Ани на', age_diff, 'год')
print( type(age_diff))