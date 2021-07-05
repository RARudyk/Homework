
# 1. Create a Vehicle class with max_speed and mileage instance attributes
print('\ntask_1')
class vehicle:
    def __init__(self, type, engine, color, max_speed, mileage):
        self.type = type
        self.engine = engine
        self.color = color
        self.max_speed = max_speed
        self.mileage = mileage
        self.speed = 0

    def accelerate(self):
        self.speed += 3
    def brake(self):
        self.speed -= 3
    def get_speed(self):
        return self.speed
    def get_mileage(self):
        return self.speed * 1.609344
    def get_max_speed(self):
        return 190
    def mi_speed(self):
        return int(self.max_speed) * 1.609344
    def get_info(self):
        print(f'I want vehicle type: {self.type}, with engine type: {self.engine} and i driving with max speed {self.max_speed} kilometr')


wv = vehicle('sedan', 'diesel' , 'green', '180', '200')

wv.accelerate()
print(f'Start drive {wv.get_speed()}')
wv.mileage
print(f'Start drive mileage {wv.get_mileage()}')
print(f'i can drive with max speed {wv.get_max_speed()} kilometr')
wv.get_info()
print(f'i can driving with max speed {wv.mi_speed()} mileage')

# 2. Create a child class Bus that will inherit all of the variables and methods of the Vehicle class and will have seating_capacity own method
print('\ntask_2')
class Bus(vehicle):
    def __init__(self, seating_capacity, type, engine, color, max_speed, mileage):
        super().__init__(type, engine, color, max_speed, mileage)
        self.seating_capacity = seating_capacity

Bohdan = Bus('35', 'Bus', 'petrol', 'yellow', '80', '100')

Bohdan.accelerate()
print(f'Drive with currently speed {Bohdan.get_speed()}')
Bohdan.get_info()
print(f'i can driving with max speed {Bohdan.mi_speed()} mileage')

# 3. Determine which class a given Bus object belongs to (Check type of an object)
print('\ntask_3')
print(type(Bus))
print(isinstance(Bohdan, Bus))

# 4. Determine if School_bus is also an instance of the Vehicle class
print('\ntask_4')
# print(issubclass(School_bus, vehicle))
# print(isinstance(School_bus, vehicle))

# 5. Create a new class School with get_school_id and number_of_students instance attributes
print('\ntask_5')
class School:
    def __init__(self, get_school_id, number_of_students):
        self.get_school_id = get_school_id
        self.number_of_students = number_of_students
    def school_name(self):
        print('Higher School named after Frank')
    def about_school(self):
        print('the school is intensively studying mathematics and English')
    def get_info(self):
        print(f'School number : {self.get_school_id} and total number of students : {self.number_of_students}')

Math_school = School('385', '2758')
Math_school.get_info()

# 6*. Create a new class SchoolBus that will inherit all of the methods from School and Bus and will have its own - bus_school_color
print('\ntask_6')
class School_bus(School, Bus):
    def __init__(self, bus_school_color, get_school_id, number_of_students,seating_capacity, type, engine, color, max_speed, mileage):
        School.__init__(get_school_id, number_of_students)
        Bus.__init__(self, seating_capacity, type, engine, color, max_speed, mileage)
        self.bus_school_color = bus_school_color
    def get_info(self):
        print('Common with School and Bus(that include vehicle class)')

#print(isinstance(School_bus, vehicle))

# 7. Polymorphism: Create two classes: Bear, Wolf. Both of them should have make_sound method. Create two instances, one of Bear and one of Wolf,
# make a tuple of it and by using for call their action using the same method.
print('\ntask_7')
class Bear:
    def __init__(self, color, age):
        self.color = color
        self.age = age
    def make_sound(self):
        print('Bear says: Grrr')
    def get_info(self):
        print(f'I am a {self.color} bear and i am {self.age} years old')

class Wolf:
    def __init__(self, color, age):
        self.color = color
        self.age = age
    def make_sound(self):
        print('Wolf says: Awwww')
    def get_info(self):
        print(f'I am a {self.color} wolf and i am {self.age} years old')

bear = Bear('broun', '27')
wolf = Wolf('gray','13')
for animals in (bear, wolf):
    animals.get_info()
    animals.make_sound()


# Magic methods:
# 8. Create class City with name, population instance attributes, return a new instance only when population > 1500,
# otherwise return message: "Your city is too small".
print('\ntask_8')
class City:

    def __new__(cls, name, population):
        if population > 1500:
            return super(City, cls).__new__(cls)
        else:
            return "Your city is too small."

    def __init__(self, name, population):
        self.name = name
        self.population = population

    def __str__(self):
        return f"Name city is {self.name} and city has population {self.population}"

town_1 = City("Kharkiv", 6000000)
print(town_1)
town_2 = City("Burshtyn", 1000)
print(town_2)

# 9. Override a printable string representation of the City class and return: The population of the city {name} is {population}
print('\ntask_9')
class City:

    def __new__(cls, name, population):
        if population > 1500:
            return super(City, cls).__new__(cls)
        else:
            return "Your city is too small."

    def __init__(self, name, population):
        self.name = name
        self.population = population

    def __str__(self):
        return f"The population of the city {self.name} is {self.population}"

town_1 = City("Kharkiv", 6000000)
print(town_1)
town_2 = City("Burshtyn", 1000)
print(town_2)

# 10*. Override magic method __add__() to perform the additional action as 'multiply' (*) the value which is greater than 10. And perform this add (+) of two instances.
print('\ntask_10')

class Math:
    def __init__(self, a):
        self.a = a
    def __add__(self, other):
        if self.a > 10 and other.a > 10:
            return self.a * other.a
        else:
            return self.a + other.a


obj1 = Math(11)
obj2 = Math(12)
obj3 = (obj1 + obj2)
print(obj3)


# 11. The __call__ method enables Python programmers to write classes where the instances behave like functions and can be called like a function.
# Create a new class with __call__ method and define this call to return sum.
print('\ntask_11')
class adding:
    def __call__(self, a, b):
        resalt = (a + b)
        return resalt

task_11 =adding()
print(task_11(3,7))

# 12*. Making Your Objects Truthy or Falsey Using __bool__().
# Create class MyOrder with cart and customer instance attributes.
# Override the __bool__magic method considered to be truthy if the length of the cart list is non-zero.
# e.g.:
# order_1 = MyOrder(['a', 'b', 'c'], 'd')
# order_2 = MyOrder([], 'a')
# bool(order_1)
# True
# bool(order_2)
# False
print('\ntask_12')
class MyOrder:
    def __init__(self, cart, customer):
        self.cart = cart
        self.customer = customer
    def __bool__(self):
        if len(self.cart) > 0:
            return True
        else:
            return False


order_1 = MyOrder(['a', 'b', 'c'], 'd')
order_2 = MyOrder([], 'a')
print(bool(order_1))
print(bool(order_2))
