import json
import os
import unittest
import task01
import task02
import gk.assignments.assignment as assignment
from gk.GkTest import GkTest


class MyTestCase(GkTest):

    def test_task_01(self):
        test_set = [0, 1, 154_950, 245_921, 1000_000, 1666862638]
        answers = {}
        for test in test_set:
            y = super().wrapper(lambda: task01.task(), test)
            answers[f"%s" % test] = y.rstrip()
        print(json.dumps(answers))
        self.assertEqual(assignment.check_assignment(11, 1, 'Seconds converter', answers), True)

    def test_task_02(self):
        test_set = [0, 1, 154_950, 245_921, 1000_000, 1666862638]
        answers = {}
        for test in test_set:
            y = super().wrapper(lambda: task02.task(), test)
            answers[f"%s" % test] = y.rstrip()
        print(json.dumps(answers))
        self.assertEqual(assignment.check_assignment(11, 2, 'Bytes converter', answers), True)


os.chdir('../..')
if __name__ == '__main__':
    unittest.main()
