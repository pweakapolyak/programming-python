

class GoodValidationError(Exception):
    def __init__(self, good):
        self.good = good

    def __str__(self):
        return "Good is not correct: " + str(self.good)


class Good:
    def __init__(self, guid, name, quantity=1):
        self.__guid = guid
        self.__name = name
        self.__quantity = quantity

    def __str__(self):
        return str(self.__guid)

    def __eq__(self, other):
        if not isinstance(other, Good):
            return False
        return self.__guid == other.__guid

    def is_valid(self):
        return True

    def get_quantity(self):
        return self.__quantity

class Alco(Good):
    def __init__(self, guid, name, legal_storage_code):
        """
        :param guid:
        :param name:
        :param legal_storage_code:
        :type legal_storage_code: str
        """
        super().__init__(guid, name)
        self.__legal_storage_code = legal_storage_code

    def is_valid(self):
        return self.__legal_storage_code.startswith("ru-159")

class Diamond(Good):
    def __init__(self, guid, name, quantity):
        super().__init__(guid, name, quantity)

    def is_valid(self):
        return super().get_quantity() < 15



class Warehouse:
    def __init__(self):
        self.__goods = []

    def print_info(self):
        print('Number of goods: ', len(self.__goods))

    def get_count(self):
        return len(self.__goods)

    def __add__(self, other):
        if isinstance(other, Good) and other.is_valid():
            self.__goods.append(other)
        else:
            raise GoodValidationError(other)
        return self

    def __sub__(self, other):
        if isinstance(other, Good):
            if other in self.__goods:
                self.__goods.remove(other)
        return self


if __name__ == "__main__":
    g1 = Good(1, "g1")
    g2 = Good(2, "g2")

    print(g1 == g1)
    print(g1 == g2)
    print(g1 == Good(1, "g1"))


    warehouse = Warehouse()
    warehouse.print_info()
    warehouse += g1
    warehouse += g2
    warehouse.print_info()
    warehouse -= Good(1, "g1")
    warehouse.print_info()

    alco1 = Alco(3, "beer", "ru-159-391")
    alco2 = Alco(3, "beer", "ru-152-391")
    warehouse += alco1

    try:
        warehouse += alco2
    except GoodValidationError as e:
        print(e.good)
    warehouse.print_info()

    d1 = Diamond(4, "saddsa", 13)
    warehouse += d1
    warehouse.print_info()