import random

class Person(object):
    def __init__(self, is_vaccinated, is_dead, is_infected):
        self._id = 0
        self.is_vaccinated = is_vaccinated
        self.is_dead = is_dead
        self.is_infected = is_infected
