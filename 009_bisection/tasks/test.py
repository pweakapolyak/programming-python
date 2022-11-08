import json
import os
import unittest
import task01
import gk.assignments.assignment as assignment
from gk.GkTest import GkTest


class MyTestCase(GkTest):

    def test_task_03(self):
        test_set = [
            (3_500_000, 350_000, 3*12),
            (3_500_000, 350_000, 12),
            (3_500_000, 350_000, 10*12),
        ]
        answers = {}
        for test in test_set:
            house_cost = test[0]
            annual_salary = test[1]
            num_of_years = test[2]
            i = 0

            def side_effect(s):
                nonlocal i, house_cost, annual_salary, num_of_years
                if i == 0:
                    i += 1
                    return house_cost
                elif i == 1:
                    i += 1
                    return annual_salary
                elif i == 2:
                    i += 1
                    return num_of_years

            y = super().wrapper_with_side_effect(lambda: task01.task(), side_effect)
            if y.rstrip().lower() != "impossible":
                answer = super().float_answer(y.rstrip().lower(), 0)
            else:
                answer = "impossible"
            answers[f"house_cost=%s_annual_salary=%s_num_of_months=%s" % test] = answer

        print(json.dumps(answers))
        self.assertEqual(assignment.check_assignment(27, 1, 'Bisection', answers), True)



os.chdir('../..')
if __name__ == '__main__':
    unittest.main()
