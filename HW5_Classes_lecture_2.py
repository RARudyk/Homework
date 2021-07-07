
#1.
print('\nTask 1')
class Laptop:
    """
    Make the class with composition.
    """
    def __init__(self):
        parth1 = Battery('Battery has one parth')
        parth2 = Battery('Battery has two parth')
        self.parths = [parth1, parth2]
class Battery:
    """
    Make the class with composition.
    """
    def __init__(self, piece):
        self.piece = piece

battery = Battery('1')


print(battery)

#2.
print('\nTask 2')
class Guitar:
    def __init__(self, name):
        self.name = name
    """
    Make the class with aggregation
    """
class GuitarString:
    def __init__(self):
        pass
    """
    Make the class with aggregation
    """

guitarstring = GuitarString()
print(guitarstring)
guitar = Guitar(guitarstring)
print(guitar)

#3.
print('\nTask 3')
class Calc:
    def __init__(self):
        adding = f"Calculation is {self}"
        return adding

    @staticmethod
    def add_num(a, b, c):
        d = (a + b + c)
        return d
calc = Calc.add_num(5, 7, 9)
print(calc)

"""
    Make class with one method "add_nums" with 3 parameters, which returns sum of these parameters.
    Note: this method should be static
"""