
class Person:
    def __init__(self, name, age, sex, weight_kg, height_cm):
        self.__name = name
        self.__age = age
        self.__sex = sex
        self.__weight_kg = weight_kg
        self.__height_cm = height_cm

    def __str__(self):
        return self.__name

    def bmi(self):
        return self.__weight_kg / (self.__height_cm/100)**2

    def get_name(self):
        return self.__name

    def sleeping_hours(self):
        return 8

    def get_age(self):
        return self.__age

class Employee(Person):
    def __init__(self, name, age, sex, weight_kg, height_cm, inn, salary):
        super().__init__(name, age, sex, weight_kg, height_cm)
        self.__inn = inn
        self.__salary = salary

    def __str__(self):
        return super().get_name() + ":" + self.__inn

class Developer(Employee):
    def __init__(self, name, age, sex, weight_kg, height_cm, inn, salary, programming_language):
        super().__init__( name, age, sex, weight_kg, height_cm, inn, salary)
        self.__programming_lang = programming_language

    def sleeping_hours(self):
        return super().sleeping_hours() - 2


p1 = Person("Denis Markov", 28, 'male', 81, 183)
print(p1)
print(p1.bmi())
print(p1.sleeping_hours())

emp1 = Employee("Denis Markov", 35, 'male', 81, 183, "125235", 150)
print(emp1)
print(emp1.bmi())
print(emp1.sleeping_hours())


dev = Developer("Denis Markov", 19, 'male', 81, 183, "125235", 150, "java")
print(dev)
print(dev.bmi())
print(dev.sleeping_hours())


def avg_age(list_persons):
    """
    :param list_persons:
    :type list_persons: list[Person]
    :return:
    """

    sum = 0
    for p in list_persons:
        sum += p.get_age()
    return sum / len(list_persons)

print(avg_age([p1, emp1, dev]))