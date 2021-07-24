import logging


class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def Error_decimal(self):
        str_a = input('first num: ')
        try:
            a = int(str_a)
        except ValueError:
            print('a is not decimal')
            logging.error('not decimal first number to add')
            return
        str_b = input('second num: ')
        try:
            b = int(str_b)
        except ValueError:
            print("b is not decimal")
            logging.error('not decimal second number to add')


    def add(self):
        logging.info("calling add_func")
        c = self.a + self.b
        print(f"{self.a} + {self.b} = {c}")
        logging.info(f"add is successfully finished, {self.a}, {self.b}")
        return c

work = Calculator()

