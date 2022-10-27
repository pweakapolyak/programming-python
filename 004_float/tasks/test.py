import json
import os
import unittest
import task01
import gk.assignments.assignment as assignment
from gk.GkTest import GkTest


class MyTestCase(GkTest):

    def test_task_01(self):
        test_set = [(250.55, 299_792_458), (250.55, 299_792_458/2), (250.55, 0), (0, 299_792_458)]
        answers = {}
        for test in test_set:
            l0 = test[0]
            v = test[1]
            i = 0

            def side_effect(s):
                nonlocal l0, v, i
                if i == 0:
                    i += 1
                    return l0
                return v

            y = super().float_answer(super().wrapper_with_side_effect(lambda: task01.task(), side_effect), nums=8)
            answers[f"l0=%s_v=%s" % (l0, v)] = str(y)
        print(json.dumps(answers))
        self.assertEqual(assignment.check_assignment(13, 1, 'General relativity', answers), True)


os.chdir('../..')
if __name__ == '__main__':
    unittest.main()
