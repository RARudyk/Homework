# Task1
# В клас калькулятора написаного на лекції, добавити функції
# пошук відсотку від числа,
# піднесення в степінь,
# взяття з під квадратного кореня
# В кожний метод добавити доктести
# Дописати юніттести для всіх методів калькулятора

import unittest
from part_1_doctest import Calc


class MyTestCase(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(Calc.sum(2, 3), 5)
        self.assertEqual(Calc.sum(-34, 274), 240)

    def test_minus(self):
        self.assertEqual(Calc.minus(23, 7), 16)
        self.assertEqual(Calc.minus(-3, -7), 4)

    def test_mul(self):
        self.assertEqual(Calc.mul(5, 5), 25)
        self.assertEqual(Calc.mul(7, 9), 63)

    def test_div(self):
        self.assertEqual(Calc.div(40, 4), 10)
        with self.assertRaises(ZeroDivisionError):
            Calc.div(13, 0)
        with self.assertRaises(TypeError):
            Calc.div(25, "5")

    def test_percent(self):
        self.assertEqual(Calc.percent(100, 25), 25)
        with self.assertRaises(TypeError):
            Calc.percent(25, "5")

    def test_exaltation(self):
        self.assertEqual(Calc.exaltation(11, 2), 121)

    def test_root(self):
        self.assertEqual(Calc.root(121), 11)




if __name__ == '__main__':
    unittest.main()
