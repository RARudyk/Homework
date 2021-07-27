# Task1
# В клас калькулятора написаного на лекції, добавити функції
# пошук відсотку від числа,
# піднесення в степінь,
# взяття з під квадратного кореня
# В кожний метод добавити доктести


class Calc:
    @staticmethod
    def sum(a, b):
        return a + b

    @staticmethod
    def minus(a, b):
        return a - b

    @staticmethod
    def mul(a, b):
        return a * b

    @staticmethod
    def div(a, b):
        return a / b

    @staticmethod
    def percent(a, b):
        print(f"пошук відсотку {b} від числа {a}")
        return a * b / 100

    @staticmethod
    def exaltation(a, b):
        print(f"піднесення числа {a} в степінь {b}")
        return a ** b

    @staticmethod
    def root(a, b = 2):
        print(f"взяття числа {a} з під квадратного кореня {b}")
        return a ** (1 / b)


obj = Calc()
print(obj.root(9))






