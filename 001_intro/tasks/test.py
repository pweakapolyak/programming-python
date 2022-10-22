import os
import unittest
import task01
import task02
import gk.assignments.assignment as assignment
from gk.GkTest import GkTest


class MyTestCase(GkTest):

    def test_task_01(self):
        print(os.getcwd())
        answers = {"16": 0, "25": 0, "0": 0, "1": 0, "2": 0}
        for key in answers:
            x = key
            y = round(float(super().wrapper(lambda: task01.task(), x)), 2)
            answers[key] = str(y)
        self.assertEqual(assignment.check_assignment(5, 1, 'Square root', answers), True)

    def test_task_02(self):
        print(os.getcwd())
        answers = {"2+2*2/2": 0}
        for key in answers:
            result = (super().wrapper(lambda: task02.task(), None))
            answers[key] = str(result).rstrip()
        self.assertEqual(assignment.check_assignment(5, 2, 'Simple calculator', answers), True)


os.chdir('../..')
if __name__ == '__main__':
    unittest.main()
