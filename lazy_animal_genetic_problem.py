# Planned on doing 2 different forms of GA for this project, but get one working first (by any reasonable means).
from typing import List, Optional

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
        self.initial_state = initial  # Make the genetic_search() function happy.
        # Can have a Goal state if unique - specified by parent class Problem.
        self.goal = None

    # The tree_key values can be used to uniquely identify states.
    # These can be utilized to specify a custom gene_pool for the genetic_search function,
    # which an instance of this class should be passed to when the GA is run.

    def actions(self, state: LazyAnimalState) -> List[str]:
        return list(self.successors.get(state.tree_key, {}).keys())

    def result(self, state: LazyAnimalState, action) -> str:
        """ Returning the state key instead of object, to work with existing genetic_search function. """
        return self.successors[state.tree_key][action]

    def value(self, state: LazyAnimalState) -> int:
        """
        fitness function: Takes a list of states,
        and returns a list of fitness values based on some (domain) logic.
        """
        subject_dict: dict = dict()
        if state.tree_key in self.utils:
            subject_dict = self.utils
        elif state.tree_key in self.successors:
            subject_dict = self.successors
        else:
            raise Exception("state.tree_key (on state passed to value fn) not found in successors or utils (second-level successors).")

        # Get the fitness value for the state passed in.
        subject_state_val: int = 0
        if isinstance(subject_dict[state.tree_key], dict):
            subject_state_val = self.recurse_to_find_subject_state_val(subject_dict[state.tree_key]) or 0
        else:
            subject_state_val = subject_dict[state.tree_key]

        # "How close are we to a goal state?":
        return abs(Constants.target_animal_kcalories - subject_state_val)

    def recurse_to_find_subject_state_val(self, subject_dict: dict, subject_state_val: Optional[int] = None) -> Optional[int]:
        for key, value in subject_dict.items():
            if isinstance(value, dict):
                self.recurse_to_find_subject_state_val(value, subject_state_val)
            elif isinstance(value, int):
                subject_state_val = value
                break
            elif isinstance(value, LazyAnimalState):
                subject_state_val = value.current_animal_kcalories
                break
            else:
                raise Exception("Unexpected value type in recurse_to_find_subject_state_val. type: ", type(value))

        return subject_state_val
