import sys

sys.path.append('aima-python')

from lazy_animal_state_helper import LazyAnimalStateHelper
from lazy_animal_genetic_problem import LazyAnimalGeneticProblem
from tests.test_search import *  # type: ignore


class RunnerGeneticGame1:

    @staticmethod
    def run_genetic():
        # See AIMA code example for a reference of how to run
        # (what params mean, etc.): test_genetic_algorithm in tests/test_search.py
        print("inside run_genetic")

        initial = LazyAnimalStateHelper.get_initial_state()
        successors = LazyAnimalStateHelper.get_successors_for_tree1()
        utils = LazyAnimalStateHelper.get_terminal_states_for_tree1()
        problem = LazyAnimalGeneticProblem(initial, successors, utils)
        genetic_search(problem, ngen=1000, pmut=0.1, n=20)
