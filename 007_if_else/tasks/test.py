import json
import os
import unittest
import task01
import task02
import task03
import task04
import gk.assignments.assignment as assignment
from gk.GkTest import GkTest


class MyTestCase(GkTest):

    def test_task_01(self):
        test_set = (-5, 0, 10, 1000, 1824, 1912, 1944, 2004, 2022, 2024, 3000, 5000)
        answers = {}
        for test in test_set:
            res = super().wrapper(lambda: task01.task(), test)
            answers[f'%s'%test] = res.rstrip().lower()
        print(json.dumps(answers))
        self.assertEqual(assignment.check_assignment(21, 1, 'Leap year', answers), True)

    def test_task_02(self):
        test_set = ('1', '9', '7', 'a', 'z', 'g', 'A', 'Z', 'G', '!', ' ', '.')
        answers = {}
        for test in test_set:
            res = super().wrapper(lambda: task02.task(), test)
            answers[f'%s' % test] = res.rstrip().lower()
        print(json.dumps(answers))
        self.assertEqual(assignment.check_assignment(21, 2, 'Digit or aplpha', answers), True)

    def test_task_03(self):
        test_set = [(0, 0), (12.25, 16.98), (912.51, 765.24), (54.20, 121) ]
        answers = {}
        for test in test_set:
            cost_price = test[0]
            sell_price = test[1]
            i = 0

            def side_effect(s):
                nonlocal i, cost_price, sell_price
                if i == 0:
                    i += 1
                    return cost_price
                return sell_price

            y = super().wrapper_with_side_effect(lambda: task03.task(), side_effect)
            answers[f"cost_price=%s_sell_price=%s" % (cost_price, sell_price)] = y.rstrip().lower()
        print(json.dumps(answers))
        self.assertEqual(assignment.check_assignment(21, 3, 'Cost/Sell', answers), True)

    def test_task_04(self):
        test_set = [
            (25, 3, 'sport', 0, 'city'),
            (25, 3, 'sport', 1, 'city'),
            (25, 3, 'minvan', 0, 'city'),
            (55, 15, 'minvan', 1, 'city'),
            (55, 10, 'minvan', 1, 'city'),
            (55, 7, 'minvan', 0, 'village'),
        ]
        answers = {}
        for test in test_set:
            age = test[0]
            exp = test[1]
            type = test[2]
            is_has_accident = test[3]
            place = test[4]
            i = 0

            def side_effect(s):
                nonlocal i, age, exp, type, is_has_accident, place
                if i == 0:
                    i += 1
                    return age
                elif i == 1:
                    i += 1
                    return exp
                elif i == 2:
                    i += 1
                    return type
                elif i == 3:
                    i += 1
                    return is_has_accident
                else:
                    return place

            y = super().wrapper_with_side_effect(lambda: task04.task(), side_effect)
            answers[f"age=%s_exp=%s_type=%s_accident=%s_place=%s" % test] = y.rstrip().lower()
        print(json.dumps(answers))
        self.assertEqual(assignment.check_assignment(21, 4, 'Decision tree', answers), True)

os.chdir('../..')
if __name__ == '__main__':
    unittest.main()
