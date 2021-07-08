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
"""
    Make class with one method "add_nums" with 3 parameters, which returns sum of these parameters.
    Note: this method should be static
"""
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

#4*.
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

#5*.
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


#6.
"""
    Create dataclass with 7 fields - key (int), name (str), phone_number (str), address (str), email (str), birthday (str), age (int)
"""
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



#7. Create the same class (6) but using NamedTuple
print('\nTask 7')
import collections

AddressBookDataClass = collections.namedtuple('AddressBookDataClass',
                                             ['key', 'name', 'phone_number', 'address',
                                              'email', 'birthday', 'age'])
a = AddressBookDataClass('23','Rom', '096-207-60-22', 'Lviv str.VV', 'r.a.rudyk@gmail.com',
                                  '23-09-1984','XX')
print(a[4])
print(a)

#8.
print('\nTask 8')
"""
    Create regular class taking 7 params on init - key, name, phone_number, address, email, birthday, age
    Make its str() representation the same as for AddressBookDataClass defined above.
"""


class AddressBook:
    def __init__(self, key, name, phone_number, address, email, birthday, age):
        self.key = key
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age

    def __str__(self):
        return f'AddressBook key:{self.key},name:{self.name},phone_number:{self.phone_number},address:{self.address},email:{self.email},birthday:{self.birthday},age:{self.age}'

a1 = AddressBook('23','Rom', '0962076022', 'Lviv', 'r.a.rudyk@gmail.com','23-09-1984','XX')

print(a1)
print(a1.key)

#9.
print('\nTask 9')
"""
Change the value of the age property of the person object
"""
# name = "John"
# age = 36
# country = "USA"


class Person:
    name = "John"
    age = 36
    country = "USA"

per = Person()
print(per.age)
per.age = 32
print(per.age)

#10.
print('\nTask 10')
"""
    
    Add an 'email' attribute of the object student and set its value
    Assign the new attribute to 'student_email' variable and print it by using getattr
    
    id = 0
    name = ""

    def __init__(self, id, name):
        self.id = id
        self.name = name
"""


class Student:
    id = 0
    name = ""

    def __init__(self, id, name):
        self.id = id
        self.name = name


    @property
    def Student_email(self):
        return self._email

    @Student_email.setter
    def Student_email(self, new):
        self._email = new



st = Student('667','Roman')
st.Student_email = 'r.a.rudyk@gmail.com'
print(st.Student_email)

#11*.
print('\nTask 10')
"""
class Celsius:
    
    By using @property convert the celsius to fahrenheit
    Hint: (temperature * 1.8) + 32)
    
    def __init__(self, temperature=0):
        self._temperature = temperature


# create an object
{obj} = ...

print({obj}.temperature)
"""
class Celsius:
    def __init__(self, temperature=0):
        self._temperature = temperature

    @property
    def fahrenheit(self):
        return ((self._temperature * 1.8) + 32)

    def fahrenheit(self, object):
        self._temperature = object
        

