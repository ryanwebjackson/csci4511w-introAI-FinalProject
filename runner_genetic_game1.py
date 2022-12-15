import sys
sys.path.append('aima-python')

from tests.test_search import *  # type: ignore


class RunnerGeneticGame1:

    @staticmethod
    def run_genetic():
        # See AIMA code example: test_genetic_algorithm
        print("inside run_genetic")

        # def genetic_search(problem, ngen=1000, pmut=0.1, n=20):
        # use this function from search.py, and pass in the problem
