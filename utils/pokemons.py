
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

    def __repr__(self):
        return self.__str__()

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

    def __lt__(self, other):
        return self.get_attack() < other.get_attack()


if __name__ == "__main__":
    print('Pokemon')