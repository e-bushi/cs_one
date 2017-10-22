import random
from person_two import Person
from virus import Virus
from logger import Logger
random.seed(4)

class Simulator(object):
    def __init__(self, population_size):
        self.population_size = population_size
        self.population = {}

        self.vaccination_rate = round(random.random(), 2)
        self.first_infected = round(random.random(), 2)

        self.initial_count_vaccinated = 0
        self.initial_count_infected = 0

        self.infected = {}
        self.vaccinated = {}
        self.healthy = {}
        self.dead = 0
        print("Population Count: {}".format(self.population_size))
        self.virus_name = input("Choose a virus type: \n(cholera, ebola, rabies, hiv, smallpox, bubonic plague, typhoid, measles, malaria)\nEnter here: ")
        self.virus = Virus(self.virus_name)
        self.virus.determine_virus()
        self.virus.virus_information()

        self.log = Logger("log_file.txt")
        self.log.write_metadata(self.population_size, self.virus_name, (self.virus.mortality_rate * 100), self.virus.basic_reproduction_rate, (self.vaccination_rate * 100))

    def create_population(self):
        _id = 0

        while _id < self.population_size:
            self.population[_id] = Person(False, False, False)
            _id += 1
        return self.population

    # def create_virus(self):
    #     virus = Virus(self.virus_name)
    #     virus.determine_virus()
    #     virus.virus_information()

    def _vaccinate(self):
        number_of_ppl_vaccinated = round(self.population_size * (self.vaccination_rate), 0)
        self.initial_count_vaccinated = number_of_ppl_vaccinated
        print("\nVaccination~")
        print("Vaccination Rate: {}%".format(self.vaccination_rate * 100))
        ppl_vaccinated = 0
        for person in self.population:
            if ppl_vaccinated == number_of_ppl_vaccinated:
                break
            else:
                self.population[ppl_vaccinated].is_vaccinated = True
                ppl_vaccinated += 1

        return self.population

    def create_vaccinated(self):
        for person in self.population:
            if self.population[person].is_vaccinated is True:
                self.vaccinated[person] = self.population.get(person)

        return self.vaccinated

    def _infect(self):
        number_of_infected = round(self.population_size * self.first_infected, 0)
        self.initial_count_infected = number_of_infected
        print("Virus Infection~")
        print("Infection Rate: {}%".format(self.first_infected * 100))
        infected = 0
        for i in self.population:

            if infected == number_of_infected:
                break
            else:
                if self.population[i].is_vaccinated is False and self.population[i].is_infected is False:
                    self.population[i].is_infected = True
                    infected += 1

        return self.population

    def create_infected(self):
        for person in self.population:
            if self.population[person].is_infected is True:
                self.infected[person] = self.population.get(person)

        return self.infected

    def create_healthy(self):
        for person in self.population:
            if self.population[person].is_infected is False and self.population[person].is_vaccinated is False:
                self.healthy[person] = self.population.get(person)

        return self.healthy


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

    def interaction(self):
        rate = round(self.virus.basic_reproduction_rate)
        per_round_log = 0
        for person_ in self.population:
            if per_round_log == round(self.initial_count_infected * 0.7):
                break

            if self.population[person_].is_infected is True:
                interation_number = 0
                per_round_log += 1
                for person in self.population:
                    random_person = random.randint(0, self.population_size - 1)

                    if interation_number == self.population_size * 0.1:
                        break
                    else:
                        if self.population[random_person].is_dead is True:
                            interation_number += 0
                        elif self.population[random_person].is_vaccinated is True and self.population[random_person].is_infected is False and self.population[random_person].is_dead is False:
                            interation_number += 1
                        elif self.population[random_person].is_infected is False and self.population[random_person].is_vaccinated is False and self.population[random_person].is_dead is False:
                            determinate = random.randint(1, 100)
                            if determinate <= self.virus.basic_reproduction_rate:
                                self.population[random_person].is_infected = True
                                self.infected[random_person] = self.population.get(random_person)
                                if random_person in self.healthy:
                                    del self.healthy[random_person]
                                self.log.log_interaction(person_, random_person, True)
                                interation_number += 1
                            else:
                                interation_number += 0
                                self.healthy[random_person]
                                self.log.log_interaction(person_, random_person, False)

                self.log.log_infection_survival(person_, self.die_or_overcome(person_))

    def die_or_overcome(self, person):
        infected_person_to_live = 0
        infected_person_to_die = 0
        died = None

        determinate = round(random.random(), 2)
        if determinate < self.virus.mortality_rate:
            died = True
            self.population[person].is_dead = True
            self.population[person].is_infected = False
            self.dead += 1

            infected_person_to_die = person
            if infected_person_to_die in self.infected:
                del self.infected[infected_person_to_die]
        else:
            died = False
            self.population[person].is_vaccinated = True
            self.vaccinated[person] = self.population.get(person)
            infected_person_to_live = person

            if infected_person_to_live in self.infected:
                del self.infected[infected_person_to_live]

        return died

    def run(self):
        time_step = 0
        while len(self.infected) is not 0:
            if len(self.healthy) == 0:
                return
            sim.interaction()
            # sim.die_or_overcome()
            time_step += 1
            self.log.log_time_step(time_step, len(self.vaccinated), len(self.infected), len(self.healthy), self.dead)



if __name__ == "__main__":
    sim = Simulator(100)
    sim.create_population()
    sim._vaccinate()
    sim.create_vaccinated()
    sim._infect()
    sim.create_infected()
    sim.create_healthy()
    sim.log_infected_and_vaccinated()
    sim.run()
    # print(sim.interaction())
    # sim.die_or_overcome()
    # print("\n\n\n\n_________________________\n\n\n\n")
    # print(sim.interaction())
    # print("--vaccinated: {}".format(len(sim.vaccinated)))
    # print("--infected: {}".format(len(sim.infected)))
    # print("--healthy: {}".format(len(sim.healthy)))
    # while len(sim.healthy) > 0 or len(sim.infected) > 0:
    #     sim.run()
