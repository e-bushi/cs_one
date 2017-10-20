import random
from person_two import Person
from virus import Virus
random.seed(4)

class Simulator(object):
    def __init__(self, population_size):
        self.population_size = population_size
        self.population = {}

        self.vaccination_rate = round(random.random(), 2)
        self.first_infected = round(random.random(), 2)

        self.virus_name = input("Choose a virus type \n(cholera, ebola, rabies, hiv, smallpox, bubonic plague, typhoid)\nEnter here: ")
        self.virus = Virus(self.virus_name)
        self.virus.determine_virus()
        self.virus.virus_information()

    def create_population(self):
        _id = 0

        while _id < self.population_size:
            self.population[_id] = Person(False, False, False)
            _id += 1
        print("Population Count: {}".format(len(self.population)))
        return self.population

    # def create_virus(self):
    #     virus = Virus(self.virus_name)
    #     virus.determine_virus()
    #     virus.virus_information()

    def _vaccinate(self):
        number_of_ppl_vaccinated = round(self.population_size * (self.vaccination_rate), 0)
        print("\nVaccination~")
        print("Vaccination Rate: {}".format(self.vaccination_rate))
        print("Number of people to be vaccinated: {}\n".format(number_of_ppl_vaccinated))
        ppl_vaccinated = 0
        for person in self.population:
            if ppl_vaccinated == number_of_ppl_vaccinated:
                break
            self.population[ppl_vaccinated].is_vaccinated = True
            ppl_vaccinated += 1

        return self.population

    def _infect(self):
        number_of_infected = round(self.population_size * self.first_infected, 0)
        print("Virus Infection~")
        print("Infection Rate: {}".format(self.first_infected))
        infected = 0
        for i in self.population:
            if infected == number_of_infected:
                break

            if self.population[i].is_vaccinated is False:
                self.population[i].is_infected = True
                infected += 1

        print("Number of infected: {}".format(number_of_infected))

        return self.population

    def log_infected_and_vaccinated(self):
        number_vacc = 0
        number_infec = 0
        regular_ppl = 0

        for person in self.population:
            if self.population[person].is_vaccinated is True:
                number_vacc += 1
            elif self.population[person].is_infected is True:
                number_infec += 1
            else:
                regular_ppl += 1

        print("\nInformation~\nVaccinated: {}\nInfected: {}\nRegular People: {}".format(number_vacc, number_infec, regular_ppl))


if __name__ == "__main__":
    sim = Simulator(2183)
    sim.create_population()
    sim._vaccinate()
    sim._infect()
    sim.log_infected_and_vaccinated()
