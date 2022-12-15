# Planned on doing 2 different forms of GA for this project, but get one working first (by any reasonable means).
from typing import List

from lazy_animal_constants import Constants
from lazy_animal_state import LazyAnimalState
from search import Problem  # type: ignore


class LazyAnimalGeneticProblem(Problem):
    """
    Note that the in this genetic Problem (algorithm),
    what is being bred together is different states and not animal instances.
    """
    def __init__(self, initial, successors, utils):
        self.successors = successors
        self.utils = utils
        self.initial = initial
        # Can have a Goal state if unique - specified by parent class Problem.
        self.goal = None

    # The tree_key values can be used to uniquely identify states.
    # These can be utilized to specify a custom gene_pool for the genetic_search function,
    # which an instance of this class should be passed to when the GA is run.

    def actions(self, state: LazyAnimalState) -> List[str]:
        return list(self.successors.get(state.tree_key, {}).keys())

    def result(self, state: LazyAnimalState, action) -> LazyAnimalState:
        return self.successors[state.tree_key][action]

    def value(self, state: LazyAnimalState):
        """
        fitness function: Takes a list of states,
        and returns a list of fitness values based on some (domain) logic.
        """
        # "How close are we to a goal state?":
        return abs(Constants.target_animal_kcalories - self.utils[state.tree_key])
