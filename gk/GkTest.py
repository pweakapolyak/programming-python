import unittest
from io import StringIO
from unittest.mock import patch


class GkTest(unittest.TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=StringIO)
    def wrapper(self, task_callback, input_data, mock_stdout):
        with patch('builtins.input', return_value=input_data):
            task_callback()
        return mock_stdout.getvalue()


if __name__ == '__main__':
    unittest.main()
