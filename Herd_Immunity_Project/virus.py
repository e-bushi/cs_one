class Virus(object):
    def __init__(self, name, mortality_rate, basic_reproduction_rate):
        self.name = name
        self.mortality_rate = mortality_rate
        self.reproduction_rate = basic_reproduction_rate
