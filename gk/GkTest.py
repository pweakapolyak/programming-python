import unittest
from io import StringIO
from unittest.mock import patch


class GkTest(unittest.TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=StringIO)
    def wrapper(self, task_callback, input_data, mock_stdout):
        with patch('builtins.input', return_value=input_data):
            task_callback()
        return mock_stdout.getvalue()

    @unittest.mock.patch('sys.stdout', new_callable=StringIO)
    def wrapper_with_side_effect(self, task_callback, side_effect_func, mock_stdout):
        with patch('builtins.input', side_effect=side_effect_func):
            task_callback()
        return mock_stdout.getvalue()

    def float_answer(self, str: str, round=2):
        try:
            return round(float(str), 2)
        except:
            return str.rstrip()


if __name__ == '__main__':
    unittest.main()
