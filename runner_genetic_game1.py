import sys
sys.path.append('aima-python')

from search import genetic_search
from lazy_animal_state_helper import LazyAnimalStateHelper
from lazy_animal_genetic_problem import LazyAnimalGeneticProblem


class RunnerGeneticGame1:

    @staticmethod
    def run_genetic():
        print("inside run_genetic")

        initial = LazyAnimalStateHelper.get_initial_state()
        successors = LazyAnimalStateHelper.get_successors_for_tree1()
        utils = LazyAnimalStateHelper.get_terminal_states_for_tree1()
        problem = LazyAnimalGeneticProblem(initial, successors, utils)
        genetic_search(
            problem,
            ngen=1000,
            pmut=0.1,
            n=20,
            recombine_fn=LazyAnimalGeneticProblem.recombine_fn,
            mutate_fn=LazyAnimalGeneticProblem.mutate_fn
        )
