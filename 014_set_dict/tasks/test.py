import json
import os
import unittest
import task01
import gk.assignments.assignment as assignment
from gk.GkTest import GkTest


class MyTestCase(GkTest):

    def test_task_1(self):
        test_set = [
            ([5, 5, 5, 3, 3, 3, 3, 1, 2, 2], 3),
            ([5, 5, 5, 3, 3, 3, 3, 1, 2, 2], 2),
            ([5, 5, 5, 3, 3, 3, 3, 1, 2, 2], 1),
            ([1, 2, 3, 2, 3, 3], 2),
            ([1], 1),
        ]
        answers = {}
        for test in test_set:
            answer = str(task01.find_n_most_common_values(test[0], test[1]))
            answers[f"arr=%s_%s" % test] = answer

        print(json.dumps(answers))
        self.assertEqual(assignment.check_assignment(41, 1, 'find_n_most_common_values', answers), True)


os.chdir('../..')
if __name__ == '__main__':
    unittest.main()
