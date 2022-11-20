
import math


class Pokemon:
    def __init__(self, name, type, attack):
        self.__name = name
        self.__type = type
        self.__attack = attack
        self.__level = 1
        self.__hp = 100
        self.__resistance_percent = .1

    def __str__(self):
        return "Pokemon<" + self.__name + ", " + self.__type + ", " + str(self.__level) + ", " \
               + str(self.__attack) + ", " + str(self.__hp) + ">"

    def evolve(self):
        self.__level += 1
        self.__attack += 5

    def do_attack(self, target_pokemon):
        """
        :param target_pokemon:
        :type target_pokemon: Pokemon
        :return:
        """
        target_pokemon.__hp -= target_pokemon.__resistance(self.__attack)

    def is_alive(self):
        return self.__hp > 0

    def __resistance(self, attack_value):
        return math.floor(attack_value - self.__resistance_percent * attack_value)

    def get_attack(self):
        return self.__attack

    def set_attack(self, new_attack):
        if isinstance(new_attack, int):
            self.__attack = new_attack



pikachu = Pokemon("Pickachu", "Electric", 35)
print(pikachu)
# pikachu.attack = 5
pikachu.evolve()
print(pikachu)

pokemon2 = Pokemon("Pokemon 2", "Fire", 40)
print(pokemon2)
pikachu.do_attack(pokemon2)
print(pokemon2)
print(pokemon2.is_alive())

pokemon2.set_attack(5)
print(pokemon2)
pokemon2.set_attack("ggg")
print(pokemon2)