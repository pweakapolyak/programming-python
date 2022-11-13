import json
import os
import unittest
import task01
import task02
import task03
import task04
import task05
import gk.assignments.assignment as assignment
from gk.GkTest import GkTest


class MyTestCase(GkTest):

    def test_task_1(self):
        test_set = [
            ("Today a perfect day", False),
            ("Apple invented IPhone", False),
            ("Apple invented IPhone", True),
            ("", False)
        ]
        answers = {}
        for test in test_set:
            answer = task01.count_a_latter(test[0], test[1])
            answers[f"%s <ignore_case: %s>" % test] = answer

        print(json.dumps(answers))
        self.assertEqual(assignment.check_assignment(35, 1, 'a letter', answers), True)

    def test_task_2(self):

        test_set = [
            "     Test  string     ",
            "  sss  ",
            "",
            "test test2"
        ]
        answers = {}
        for test in test_set:
            answer = task02.trim(test)
            answers[f"%s" % test] = answer

        print(json.dumps(answers))
        self.assertEqual(assignment.check_assignment(35, 2, 'trim', answers), True)

    def test_task_3(self):

        test_set = [
            "   word word  word word    ",
            "word word  ",
            "",
            "word word"
        ]
        answers = {}
        for test in test_set:
            answer = task03.word_count(test)
            answers[f"%s" % test] = answer

        print(json.dumps(answers))
        self.assertEqual(assignment.check_assignment(35, 3, 'word count', answers), True)

    def test_task_4(self):

        test_set = [
            "apple",
            "test",
            "world",
            "zoo"
        ]
        answers = {}
        for test in test_set:
            encoded = task04.encode(test)
            answer = task04.decode(encoded)
            answers[f"%s" % test] = answer

        print(json.dumps(answers))
        self.assertEqual(assignment.check_assignment(35, 4, 'encode', answers), True)

    def test_task_5(self):

        test_set = [
            """<div class="pricesRow___SbwZq">
    <div class="price___RlZlW">
        <div class="visuallyHidden___Fxmpo">Текущая цена</div>
        <span class="hidden___iCrIR">Цена </span>
        <meta itemprop="priceCurrency" content="AMD">
        <meta itemprop="priceValidUntil" content="2023-11-12">
        <span itemprop="price" content="45579">45&nbsp;579&nbsp;AMD</span>
    </div>
</div>"""
        ]
        answers = {}
        for test in test_set:
            answer = task05.parse_price_from_document(test)
            answers["price_document.html"] = answer

        print(json.dumps(answers))
        self.assertEqual(assignment.check_assignment(35, 5, 'parse document', answers), True)


os.chdir('../..')
if __name__ == '__main__':
    unittest.main()
