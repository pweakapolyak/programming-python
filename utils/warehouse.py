



class Good:
    def __init__(self, guid, name):
        self.__guid = guid
        self.__name = name

    def __eq__(self, other):
        if not isinstance(other, Good):
            return False
        return self.__guid == other.__guid


class Warehouse:
    def __init__(self):
        self.__goods = []

    def print_info(self):
        print('Number of goods: ', len(self.__goods))

    def __add__(self, other):
        if isinstance(other, Good):
            self.__goods.append(other)
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