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


class Animal:

    def __init__(self, power: int, speed: int):
        self.id = None
        self.max_power = power
        self.current_power = power
        self.speed = speed

    def eat(self, forest: Forest):
        pass


class Predator:

    def eat(self, forest: Forest):
        pass


class Herbivorous:

    def eat(self, forest: Forest):
        pass


AnyAnimal = Any[Herbivorous, Predator]


class Forest:

    def __init__(self):
        self.animals: Dict[str, AnyAnimal] = dict()

    def add_animal(self, animal: AnyAnimal):
        pass

    def remove_animal(self, animal: AnyAnimal):
        pass


def animal_generator():
    pass
