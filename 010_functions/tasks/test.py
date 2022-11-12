import json
import os
import unittest
import task01
import task02
import task03
import gk.assignments.assignment as assignment
from gk.GkTest import GkTest


class MyTestCase(GkTest):

    def test_task_1(self):
        test_set = [
            (5, 10),
            (10, 5),
            (0, 0),
            (-1, -2),
            (2.35, 2.351)
        ]
        answers = {}
        for test in test_set:

            answer = task01.max(test[0], test[1])
            answers[f"max_%s_%s" % test] = answer

        print(json.dumps(answers))
        self.assertEqual(assignment.check_assignment(30, 1, 'Max', answers), True)


    def test_task_2(self):

        answers = {}
        for n in range(1, 21):
            answer = task02.fibonacci(n)
            answers[f"fibonacci_%s" % n] = answer

        print(json.dumps(answers))
        self.assertEqual(assignment.check_assignment(30, 2, 'Fibonacci', answers), True)

    def test_task_3(self):

        answers = {}
        for n in range(-1, 366):
            answer1 = task03.get_month_by_day_number(n, True)
            answer2 = task03.get_month_by_day_number(n, False)
            answers[f"day_%s_is_leap_%s" % (n, True)] = answer1
            answers[f"day_%s_is_leap_%s" % (n, False)] = answer2

        print(json.dumps(answers))
        self.assertEqual(assignment.check_assignment(30, 3, 'Months', answers), True)



os.chdir('../..')
if __name__ == '__main__':
    unittest.main()
