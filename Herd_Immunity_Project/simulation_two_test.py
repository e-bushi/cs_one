import pytest
from simulation_two import Simulator

def create_sim_instance():
    sim = Simulator(1000)
    return sim

def sim_test():
    sim = create_sim_instance()
    assert sim.population_size == 1000
    assert len(sim.population) == 1000
