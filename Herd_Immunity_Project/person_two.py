import random

class Person(object):
    def __init__(self, is_vaccinated, is_alive):
        self._id = 0
        self.is_vaccinated = False
        self.is_dead = False
        self.is_infected = False
