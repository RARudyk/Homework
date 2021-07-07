
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


#4*.
print('\nTask 4')
class Pasta:
    def __init__(self, ingredients):
        self.ingredients = ingredients
#    def __str__(self):
#        return f"Pasta includes ingredients: {self.ingredients}"
    def __repr__(self):
        return f"Pasta ({self.ingredients})"
    @classmethod
    def carbonara(cls, ingredient):
        i = ['forcemeat', 'tomatoes'].append(ingredient)
        return cls(i)
    @classmethod
    def bolognaise(cls):
        d = ['bacon', 'parmesan', 'eggs']
        return cls(d)

pasta_1 = Pasta(["tomato", "cucumber"])
print(pasta_1)
pasta_2 = Pasta.bolognaise()
print(pasta_2)
"""
    Make class which takes 1 parameter on init - list of ingredients and defines instance attribute ingredients.
    It should have 2 methods:
    carbonara (['forcemeat', 'tomatoes']) and bolognaise (['bacon', 'parmesan', 'eggs'])
    which should create Pasta instances with predefined list of ingredients.
    Example:
        pasta_1 = Pasta(["tomato", "cucumber"])
        pasta_1.ingredients will equal to ["tomato", "cucumber"]
        pasta_2 = Pasta.bolognaise()
        pasta_2.ingredients will equal to ['bacon', 'parmesan', 'eggs']
"""

#5*.
print('\nTask 5')
class Concert:
    max_visitor_num = 0
    def __init__(self, visitors_count = 0):
        self.visitors_count = visitors_count
    @property
    def visitors_count(self):
        return f"Max visitors number: {self._visitors_count}"

    @visitors_count.setter
    def visitors_count(self, v_count):
        if v_count > self.max_visitor_num:
            self._visitors_count = self.max_visitor_num
        else:
            self._visitors_count = v_count


Concert.max_visitor_num = 50
concert = Concert()
concert.visitors_count = 1000
print(concert.visitors_count)

"""
    Make class, which has max_visitors_num attribute and its instances will have visitors_count attribute.
    In case of setting visitors_count - max_visitors_num should be checked,
    if visitors_count value is bigger than max_visitors_num - visitors_count should be assigned with max_visitors_num.
    Example:
        Concert.max_visitor_num = 50
        concert = Concert()
        concert.visitors_count = 1000
        print(concert.visitors_count)  # 50
"""

#6.
print('\nTask 6')
import dataclasses

@dataclasses.dataclass
class AddressBookDataClass:
    key: int
    name: str
    phone_number :str
    address: str
    email: str
    birthday :str
    age: int

"""
    Create dataclass with 7 fields - key (int), name (str), phone_number (str), address (str), email (str), birthday (str), age (int)
"""

#7. Create the same class (6) but using NamedTuple
print('\nTask 7')
import collections

AddressBookDataClass = collections.namedtuple('AddressBookDataClass',
                                             ['key', 'name', 'phone_number', 'address',
                                              'email', 'birthday', 'age'])


