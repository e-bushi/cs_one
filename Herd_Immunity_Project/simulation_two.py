import random
from person_two import Person
from virus import Virus

class simulator(object):
    def __init__(self, population_size):
        self.population_size = population_size
        self.population = {}

        self.vaccination_rate = int(input("What percent of people are vaccinated?: "))

        self.virus_name = ""
        self.mortality_rate = 0.0
        self.basic_reproduction_rate = 0.0
        self.determine_virus()

    def create_population(self):
        _id = 1
        if _id < len(self.population):
            self.population[_id] = Person(False, False)
            _id += 1

    def determine_virus(self):
        name = input("What is the name of the virus: ")
        mort_rate = int(input("What is the mortality rate of the virus: "))
        basic_repro = int(input("What is the reproduction rate of the virus?: "))

        self.virus_name = name
        self.mortality_rate = mort_rate
        self.basic_reproduction_rate = basic_repro

        virus_object = Virus(self.virus_name, self.mortality_rate, self.basic_reproduction_rate)

    def infection_or_vaccinate():
        number_of_ppl_vaccinated = len(self.population) * (self.vaccination_rate / 100)
        ppl_vaccinated = 0
        for person in self.population:
            self.population[ppl_vaccinated].is_vaccinated = True
            ppl_vaccinated += 1
