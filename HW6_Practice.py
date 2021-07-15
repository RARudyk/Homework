from abc import abstractmethod


class GardenMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Garden(metaclass=GardenMeta):
    def __init__(self, vegetables, fruits):
        self.vegetables = vegetables
        self.fruits = fruits

    def show_the_garden(self):
        print(f'I have such vegetables {self.vegetables}')
        print(f'I have such fruits {self.fruits}')


class Vegetables:
    def __init__(self, vegetable_type):
        self.vegetable_type = vegetable_type

    states = {"0": "None", "1": "Flowering", "2": "Green", "3": "Red"}

    @abstractmethod
    def growth(self):
        raise NotImplementedError('You missed me.')

    @abstractmethod
    def is_ripe(self):
        raise NotImplementedError("You missed me")


class Fruits:
    def __init__(self, fruits_type):
        self.fruits_type = fruits_type

    states = {0: "None", 1: "Flowering", 2: "Green", 3: "Red"}

    @abstractmethod
    def growth(self):
        raise NotImplementedError('You missed me.')

    @abstractmethod
    def is_ripe(self):
        raise NotImplementedError("You missed me")


class Tomato(Vegetables):
    def __init__(self, vegetable_type, number_of_tomatoes):
        # super(Vegetables, self).__init__(vegetables_type)
        Vegetables.__init__(self, vegetable_type)
        self.number_of_tomatoes = number_of_tomatoes
        self.states = 0
        self.vegetable_type = vegetable_type

    def growth(self):
        if self.states < 3:
            self.states += 1
        self.print_state()

    def print_state(self):
        print(f"{self.vegetable_type}, {self.number_of_tomatoes} , {self.states}")

    def is_ripe(self):
        return self.states == 3

    def pests_eating(self):
        self.states = 0

    """
    def is_ripe(self):
        if self.states == 3:
            return True
        return Fasle
    """


class Apple(Fruits):
    def __init__(self, fruits_type, number_of_apples):
        Fruits.__init__(self, fruits_type)
        self.number_of_apples = number_of_apples
        self.states = 0
        self.fruits_type = fruits_type

    def print_state(self):
        print(f"{self.fruits_type}, {self.number_of_apples} , {self.states}")

    def growth(self):
        if self.states < 3:
            self.states += 1
        self.print_state()

    def is_ripe(self):
        return self.states == 3

    def pests_eating(self):
        self.states = 0


class TomatoBush:
    def __init__(self, number_of_tomatoes):
        # lst = []
        # for num in range(number_of_tomatoes):
        #   tamato = Tomatoes('Cherry', num)
        #   t1 = Tomatoes('Cerry',1)
        #    lst.append(t1)
        self.tomatoes = [Tomato('Cherry', index) for index in range(0, number_of_tomatoes - 1)]

    def growth_all(self):
        for tomato in self.tomatoes:
            tomato.growth()

            # def all_are_ripe(self):
            #   lst = []
            #   for tomato in self.tomatoes:
            #     ripe_state = tomato.is_ripe()
            #       lst.append(ripe_state)
            #   return all(lst) # якщо всі дозрілі True якщо ні False
            # потрібний лише результат True or False

    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    def give_away_all(self):
        self.tomatoes = []

    def pests_eat_tomato(self):
        for tomato in self.tomatoes:
            if tomato.states == [2, 3]:
                tomato.pests_eating()
            else:
                print('Green tomato')


class AppleTree:
    def __init__(self, number_of_apples):
        self.apples = [Apple('White', index) for index in range(0, number_of_apples - 1)]

    def growth_all(self):
        for apple in self.apples:
            apple.growth()

    def all_are_ripe(self):
        return all([apple.is_ripe() for apple in self.apples])

    def give_away_all(self):
        self.apples = []

    def pests_eat_apple(self):
        for apple in self.apples:
            if apple.states == 3:
                apple.pests_eating()
            else:
                print('Green apple')


class Gardener:
    def __init__(self, name, plants):
        self.name = name
        self.plants = plants
        self.worm = 0
        # self.quantity = Pests(self.quantity)

    def work(self):
        for plant in self.plants:
            plant.growth_all()

    def harvest(self):
        for plant in self.plants:
            if plant.all_are_ripe():
                plant.give_away_all()
            else:
                print('Too early to harvest')


class Pests:
    def __init__(self, quantity):
        self.quantity = quantity

    @abstractmethod
    def eat_plants(self):
        raise NotImplementedError('No pests.')

    def raise_pests(self):
        self.quantity += 1
        print(f'Pests growing and now their {self.quantity}')

    @abstractmethod
    def poison_pests(self):
        raise NotImplementedError('No pests.')


class ApplePests(Pests):
    def __init__(self, pests_type, quantity):
        Pests.__init__(self, quantity)
        self.pests_type = pests_type
        self.quantity = quantity

    def eat_plants(self):
        for plant in self.quantity:
            if self.quantity > 4:
                plant.pests_eat_apple()
                print('Very nice apple')
            else:
                print(f'We do not enough pests, {self.quantity}')

    def poison_pests(self):
        if self.quantity == 3:
            print(f'We have only {self.quantity} pests')
        elif self.quantity == 4:
            self.quantity //= 2
            print(f'Gardener killed half pests because some amount {self.quantity} '
                  f'of them needs for indication herbicide influence on plants')
        elif self.quantity == 15:
            print(f'Gardener thought about poison for pests')
        else:
            self.quantity = []
            print(f'Gardener cleaned our garden of pests and pests quantity now is {self.quantity}')


class TomatoPests(Pests):
    def __init__(self, pests_type, quantity):
        Pests.__init__(self, quantity)
        self.pests_type = pests_type
        self.quantity = quantity

    def eat_plants(self):
        for plant in self.quantity:
            if self.quantity > 4:
                plant.pests_eat_tomato()
                print('Very nice tomato')
            else:
                print(f'We do not enough pests, {self.quantity}')

    def poison_pests(self):
        if self.quantity == 3:
            print(f'We have only {self.quantity} pests')
        elif self.quantity == 4:
            self.quantity //= 2
            print(f'Gardener killed half pests because some amount {self.quantity} '
                  f'of them needs for indication herbicide influence on plants')
        elif self.quantity == 15:
            print(f'Gardener thought about poison for pests')
        else:
            self.quantity = []
            print(f'Gardener cleaned our garden of pests and pests quantity now is {self.quantity}')






tomato1 = TomatoBush(9)
apple_tree1 = AppleTree(7)

John = Gardener('John', [tomato1, apple_tree1])
garden1 = Garden(tomato1, apple_tree1)

John.work()
John.work()
John.work()


apple_pests = ApplePests('caterpillar', 2)
apple_pests.raise_pests()
apple_pests.raise_pests()
apple_pests.poison_pests()

apple_tree1.pests_eat_apple()

tomato_pests = TomatoPests('Worm', 10)
tomato_pests.raise_pests()
tomato_pests.raise_pests()

tomato1.pests_eat_tomato()

tomato_pests.poison_pests()

John.harvest()

print(tomato1.tomatoes)
print(apple_tree1.apples)
