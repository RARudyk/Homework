# Survival
#
# 1. In the Forest (Iterable) lives Predators and Herbivores (abstract class of animal and two offspring).
# Each animal is born with the following parameters (by using random):
# - strength (from 25 to 100 points)
# - speed (from 25 to 100 points)
# The force cannot be greater than it was at birth (initialization).
#
# At each step of the game we take 1 animal from the forest (iteration):
# - If it is herbivorous, then it eats (restores its strength by 50%).
# - If it is a predator, it hunts - randomly chooses an animal from the forest and:
#     - pulled himself out, he was unlucky and he was left without a dinner;
#     - pulled out another animal, then tries to catch up;
#     - if he can catch up, he catches up and attacks;
#     - if attacked and is stronger, then eats and restores 50% of strength;
#     - did not catch up or did not have enough strength,
#       then he and the lucky prey lose 30% of strength
#       (Because both either ran, or fought, or all together)
#
# An animal whose power has expired dies. (You can check the strength at the time of food search)
# The game continues as long as predators are present in the forest.
# Tips:
# When a predator hunts, an animal is accidentally taken from the forest.
# This animal may be the predator itself. To check this and distinguish two animals with the same characteristics,
# use the uuid library. But when creating an animal, assign its id a unique value.
#
# You can use the random library to work with random numbers

from __future__ import annotations
from typing import Dict, Any
from abc import ABC, abstractmethod
import random
import uuid
import time


class Animal(ABC):

    def __init__(self, power: int, speed: int):
        self.id = None
        self.max_power = power
        self.current_power = power
        self.speed = speed

    @abstractmethod
    def eat(self, forest: Forest):
        raise NotImplementedError('Not implemented')


class Predator(Animal):

    def eat(self, forest: Forest):
        booty = random.choice(list(forest.animals.values()))
        if booty.id == self.id:
            print("No booty found, predator left without food")
        else:
            print(f"{__class__.__name__} with {self.current_power} power and {self.speed} speed "
                  f"starts hunting for booty {booty.__class__.__name__} with {booty.current_power} power and {booty.speed} speed")
            if self.speed > booty.speed:
                print("Predator caught the booty")
                if self.current_power > booty.current_power:
                    print("Predator won and eats the booty")
                    won(booty)
                    power_up(self)
                else:
                    print("Predator lost in battle")
                    beat(self)
                    beat(booty)
            else:
                print("The booty ran away")
                failed_hunting(self)
                failed_hunting(booty)


class Herbivorous(Animal):

    def eat(self, forest: Forest):
        power_up(self)


def power_up(animal: AnyAnimal):
    print(f"{animal.__class__.__name__} is eating with {animal.current_power} power")
    if animal.current_power + animal.max_power * 0.5 >= animal.max_power:
        animal.current_power = animal.max_power
    else:
        animal.current_power = round(animal.current_power + animal.max_power * 0.5, 1)
    print(f"{animal.__class__.__name__} ate and recovered power to {animal.current_power}")


def won(herbivorous: AnyAnimal):
    forest.remove_animal(herbivorous)
    print(f"{herbivorous.__class__.__name__} died")


def beat(animal: AnyAnimal):
    if animal.current_power - animal.max_power * 0.3 <= 0:
        forest.remove_animal(animal)
        print(f"{animal.__class__.__name__} died in a battle")

    else:
        animal.current_power = round(animal.current_power - animal.max_power * 0.3, 1)
        print(f"{animal.__class__.__name__} lost battle with {animal.current_power} power left")


def failed_hunting(animal: AnyAnimal):
    if animal.current_power - animal.max_power * 0.3 <= 0:
        forest.remove_animal(animal)
        print(f"{animal.__class__.__name__} died in a battle")

    else:
        animal.current_power = round(animal.current_power - animal.max_power * 0.3, 1)
        print(f"{animal.__class__.__name__} has {animal.current_power} power left after failed chase")


AnyAnimal: Any[Herbivorous, Predator]


class Forest:
    def __init__(self):
        self.animals: Dict[str, AnyAnimal] = dict()

    def add_animal(self, animal: AnyAnimal):
        print(f"New animal added to the forest", animal)
        self.animals.update({animal.id: animal})

    def remove_animal(self, animal: AnyAnimal):
        print(f"{animal.__class__.__name__} removed from the forest")
        self.animals.pop(animal.id)

    def any_predator_left(self):
        for x in list(self.animals.values()):
            if x.__class__.__name__ == "Predator":
                print(f"{x.__class__.__name__} is in the forest")
                return True
        print(f"Only {x.__class__.__name__} live in the forest")
        return False


def animal_generator():
    while True:
        generated_animal = random.choice((Predator(random.randint(25, 100), random.randint(25, 100)),
                                          Herbivorous(random.randint(25, 100), random.randint(25, 100))))
        generated_animal.id = uuid.uuid4()
        yield generated_animal


if __name__ == "__main__":
    forest = Forest()
    nature = animal_generator()

    for i in range(10):
        animal = next(nature)
        print(animal.__dict__)
        forest.add_animal(animal)
    print([{x.__class__.__name__: x.__dict__} for x in list(forest.animals.values())])

    while True:
        if not forest.any_predator_left():
            break
        random.choice(list(forest.animals.values())).eat(forest)
        time.sleep(1)
