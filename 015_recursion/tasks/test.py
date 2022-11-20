import json
import os
import unittest
import task01
import gk.assignments.assignment as assignment
from gk.GkTest import GkTest


class MyTestCase(GkTest):

    def test_task_1(self):
        test_set = [
            "tea",
            "abc",
            "ball",
            ""
        ]
        answers = {}
        for test in test_set:
            answer = str(task01.permutation(test))
            answers[f"word_%s" % test] = answer

        print(json.dumps(answers))
        self.assertEqual(assignment.check_assignment(44, 1, 'permutation', answers), True)


os.chdir('../..')
if __name__ == '__main__':
    unittest.main()
