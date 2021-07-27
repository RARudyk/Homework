# Task1
# В клас калькулятора написаного на лекції, добавити функції
# пошук відсотку від числа,
# піднесення в степінь,
# взяття з під квадратного кореня
# В кожний метод добавити доктести


class Calc:
    @staticmethod
    def sum(a, b):
        """
        >>> Calc.sum(23, 7)
        30

        """
        return a + b

    @staticmethod
    def minus(a, b):
        """
        >>> Calc.minus(10, 3)
        7

        """
        return a - b

    @staticmethod
    def mul(a, b):
        """
        >>> Calc.mul(4, 2)
         8

        """
        return a * b

    @staticmethod
    def div(a, b):
        """
        >>> Calc.div(25, 5)
        5.0

        """
        return a / b

    @staticmethod
    def percent(a, b):
        """
        >>> Calc.percent(45, 10)
        4.5

        """
        # print(f"пошук відсотку {b} від числа {a}")
        return a * b / 100

    @staticmethod
    def exaltation(a, b) -> int:
        """
        >>> Calc.exaltation(5, 2)
        25

        """
        # print(f"піднесення числа {a} в степінь {b}")
        return a ** b

    @staticmethod
    def root(a, b = 2) -> float:
        """
        >>> Calc.root(121, 2)
        11.0

        """
        # print(f"взяття числа {a} з під квадратного кореня {b}")
        return a ** (1 / b)


obj = Calc()
print(obj.root(9))






