import json
import os
import unittest
import task01
import task02
import task03
import task04
import task05
import task06
import gk.assignments.assignment as assignment
from gk.GkTest import GkTest


class MyTestCase(GkTest):

    def test_task_1(self):
        test_set = [
            (task01.min_abs, [-1, 0, 10, 100]),
            (task01.max_abs, [-1, 0, 10, 100]),
            (task01.max_abs, [-1, 0, 10, 100, -600, 599]),
            (task01.min_abs, [-1, 0, 10, 100, -600, 599]),
            (task01.max_abs, []),
            (task01.min_abs, []),
        ]
        answers = {}
        for test in test_set:
            answer = test[0](test[1])
            answers[f"arr=%s_%s" % (test[1], "min" if test[0] == task01.min_abs else "max")] = answer

        print(json.dumps(answers))
        self.assertEqual(assignment.check_assignment(38, 1, 'min/max', answers), True)

    def test_task_2(self):
        test_set = [
            [1, 2, 3, 4, 5],
            [2, 4, 6],
            [],
            [1, 3, 5]
        ]
        answers = {}
        for test in test_set:
            answer = str(task02.filter_odd(test))
            answers[f"arr=%s" % test] = answer

        print(json.dumps(answers))
        self.assertEqual(assignment.check_assignment(38, 2, 'filter odd', answers), True)

    def test_task_3(self):
        test_set = [
            [-1, -2, -3, 0, 4, 5],
            [1, 2, 3, 4],
            [],
            [-10, -15]
        ]
        answers = {}
        for test in test_set:
            answer = str(task03.negative_sum(test))
            answers[f"arr=%s" % test] = answer

        print(json.dumps(answers))
        self.assertEqual(assignment.check_assignment(38, 3, 'negative sum', answers), True)

    def test_task_4(self):
        test_set = [
            [5, 5, 5, 10, 10, 2, 2, 2, 0, 2],
            [-1, 1, 5, 5, 0, 0, 0, 5, 1, 5],
            [],
            [-1, -1, 0, 0, -1]
        ]
        answers = {}
        for test in test_set:
            answer = str(task04.moda(test))
            answers[f"arr=%s" % test] = answer

        print(json.dumps(answers))
        self.assertEqual(assignment.check_assignment(38, 4, 'moda', answers), True)

    def test_task_5(self):
        os.chdir('./013_list/tasks')
        test_set = [
            "a*p**e",
            "th*",
            "test",
            "***ter"
        ]
        answers = {}
        for test in test_set:
            answer = str(task05.search_by_pattern(test))
            answers[f"pattern=%s" % test] = answer

        os.chdir('../..')
        print(json.dumps(answers))
        self.assertEqual(assignment.check_assignment(38, 5, 'search by pattern', answers), True)

    def test_task_6(self):
        os.chdir('./013_list/tasks')
        answers = {}
        answer = self.float_answer(task06.find_avg_salary(), 2)
        answers[f"answer"] = answer

        os.chdir('../..')
        print(json.dumps(answers))
        self.assertEqual(assignment.check_assignment(38, 6, 'avg salary', answers), True)


os.chdir('../..')
if __name__ == '__main__':
    unittest.main()
