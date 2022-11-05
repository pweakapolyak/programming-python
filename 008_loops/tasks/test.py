import json
import os
import unittest
import task01
import task02
import task03
import task04
import task05
import gk.assignments.assignment as assignment
from gk.GkTest import GkTest


class MyTestCase(GkTest):

    def test_task_01(self):
        answers = {}
        res = super().wrapper(lambda: task01.task(), "")
        answers['result'] = res.rstrip().lower()
        print(json.dumps(answers))
        self.assertEqual(assignment.check_assignment(24, 1, 'List numbers', answers), True)

    def test_task_02(self):
        answers = {}
        res = super().wrapper(lambda: task02.task(), "")
        answers['result'] = res.rstrip().lower()
        print(json.dumps(answers))
        self.assertEqual(assignment.check_assignment(24, 2, 'List numbers reverse', answers), True)

    def test_task_03(self):
        test_set = [
            (14_000_000, 2_240_000, 25),
            (19_000_000, 5_240_000, 10),
            (10_000_000, 5_240_000, 45),
            (3_000_000, 1_240_000, 65),
        ]
        answers = {}
        for test in test_set:
            house_cost = test[0]
            annual_salary = test[1]
            percent_saved = test[2]
            i = 0

            def side_effect(s):
                nonlocal i, house_cost, annual_salary, percent_saved
                if i == 0:
                    i += 1
                    return house_cost
                elif i == 1:
                    i += 1
                    return annual_salary
                elif i == 2:
                    i += 1
                    return percent_saved

            y = super().wrapper_with_side_effect(lambda: task03.task(), side_effect)
            answers[f"house_cost=%s_annual_salary=%s_percent_saved=%s" % test] = y.rstrip().lower()
        print(json.dumps(answers))
        self.assertEqual(assignment.check_assignment(24, 3, 'Down payment', answers), True)

    def test_task_04(self):
        test_set = [
            (14_000_000, 2_240_000, 25, 5),
            (19_000_000, 5_240_000, 10, 4,),
            (10_000_000, 5_240_000, 45, 2),
            (3_000_000, 1_240_000, 65, 10),
        ]
        answers = {}
        for test in test_set:
            house_cost = test[0]
            annual_salary = test[1]
            percent_saved = test[2]
            semi_annual_raise_percent = test[3]
            i = 0

            def side_effect(s):
                nonlocal i, house_cost, annual_salary, percent_saved, semi_annual_raise_percent
                if i == 0:
                    i += 1
                    return house_cost
                elif i == 1:
                    i += 1
                    return annual_salary
                elif i == 2:
                    i += 1
                    return percent_saved
                elif i == 3:
                    i += 1
                    return semi_annual_raise_percent

            y = super().wrapper_with_side_effect(lambda: task04.task(), side_effect)
            answers[
                f"house_cost=%s_annual_salary=%s_percent_saved=%s_semi_annual_raise_percent=%s" % test] = y.rstrip().lower()
        print(json.dumps(answers))
        self.assertEqual(assignment.check_assignment(24, 4, 'Down payment #2', answers), True)

    def test_task_05(self):
        test_set = (0, 1, 5, 10)
        answers = {}
        for test in test_set:
            res = super().wrapper(lambda: task05.task(), test)
            answers[f'%s' % test] = res.rstrip().lower()
        print(json.dumps(answers))
        self.assertEqual(assignment.check_assignment(24, 5, 'Inner loop', answers), True)


os.chdir('../..')
if __name__ == '__main__':
    unittest.main()
