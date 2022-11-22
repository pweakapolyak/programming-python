import unittest
from utils.warehouse import Warehouse, Good, Diamond, GoodValidationError


class WarehouseTest(unittest.TestCase):


    def test_add_to_warehouse(self):

        # init
        warehouse = Warehouse()
        g1 = Good(123, "test")
        g2 = Good(1234, "test")

        # when
        warehouse += g1
        warehouse += g2

        # then
        self.assertEqual(warehouse.get_count(), 2)

        return

    def test_should_not_add_not_valid_good(self):
        # init
        warehouse = Warehouse()
        valid_good = Good(123, "test")
        warehouse += valid_good

        not_valid_good = Diamond(1, "test", 30)

        # when/then
        self.assertRaises(GoodValidationError, warehouse.__add__, not_valid_good)
        self.assertEqual(warehouse.get_count(), 1)

