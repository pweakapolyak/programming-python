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
        test_set = (-5, 0, 10, 100, 150, 400, 500, 1_000_000)
        answers = {}
        for test in test_set:
            res = super().wrapper(lambda: task01.task(), test)
            answers[f'num_%s'%test] = res.rstrip()
        print(json.dumps(answers))
        self.assertEqual(assignment.check_assignment(16, 1, 'Interval 01', answers), True)

    def test_task_02(self):
        test_set = (-5, 0, 10, 100, 150, 400, 500, 1_000_000)
        answers = {}
        for test in test_set:
            res = super().wrapper(lambda: task02.task(), test)
            answers[f'num_%s'%test] = res.rstrip()
        print(json.dumps(answers))
        self.assertEqual(assignment.check_assignment(16, 2, 'Interval 02', answers), True)

    def test_task_03(self):
        test_set = (-5, 0, 10, 100, 150, 400, 500, 1_000_000)
        answers = {}
        for test in test_set:
            res = super().wrapper(lambda: task03.task(), test)
            answers[f'num_%s'%test] = res.rstrip()
        print(json.dumps(answers))
        self.assertEqual(assignment.check_assignment(16, 3, 'Interval 03', answers), True)

    def test_task_04(self):
        test_set = [(650_000, 18, 0), (250_000, 19, 1), (500_001, 25, 0), (0, 32, 1), (0, 32, 0)]
        answers = {}
        for test in test_set:
            sal = test[0]
            age = test[1]
            is_has_possessions = test[2]
            i = 0

            def side_effect(s):
                nonlocal i, sal, age, is_has_possessions
                if i == 0:
                    i += 1
                    return sal
                elif i == 1:
                    i += 1
                    return age
                return is_has_possessions

            y = super().wrapper_with_side_effect(lambda: task04.task(), side_effect)
            answers[f"sal=%s_age=%s_possessions=%s" % (sal, age, is_has_possessions)] = y.rstrip()
        print(json.dumps(answers))
        self.assertEqual(assignment.check_assignment(16, 4, 'Credit scoring', answers), True)


os.chdir('../..')
if __name__ == '__main__':
    unittest.main()
