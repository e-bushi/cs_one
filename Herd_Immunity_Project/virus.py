class Virus(object):
    def __init__(self, name):
        self.name = name
        self.mortality_rate = 0.0
        self.basic_reproduction_rate = 0.0

    def determine_virus(self):
        # name = input("Choose a virus type \n(cholera, ebola, rabies, hiv, smallpox, bubonic plague, typhoid)\nEnter here: ")

        if self.name == "cholera":
            self.mortality_rate = .01
            self.basic_reproduction_rate = 2.0
        elif self.name == "ebola":
            self.mortality_rate = 0.7
            self.basic_reproduction_rate = 2.4
        elif self.name == "rabies":
            self.mortality_rate = 1.0
            self.basic_reproduction_rate = 1.3
        elif self.name == "hiv":
            self.mortality_rate = 0.8
            self.basic_reproduction_rate = 3.5
        elif self.name == "smallpox":
            self.mortality_rate = .15
            self.basic_reproduction_rate = 6.0
        elif self.name == "bubonic plague":
            self.mortality_rate = 0.6
            self.basic_reproduction_rate = 1.0
        elif self.name == "typhoid":
            self.mortality_rate = 0.2
            self.basic_reproduction_rate = 2.5
        elif self.name == "measles":
            self.mortality_rate = 0.001
            self.basic_reproduction_rate = 15.0
        elif self.name == "malaria":
            self.mortality_rate = 0.0015
            self.basic_reproduction_rate = 16.0
        else:
            print("That's not a choice. Make sure to check your spelling and that everything is lowercase")

    def virus_information(self):
        print("\nVirus Name: {}\nVirus Mortality Rate: {}\nVirus Basic Reproduction Rate: {}".format(self.name, self.mortality_rate, self.basic_reproduction_rate))
