from random import *
from typing import List, Optional, Tuple

from lazy_animal_constants import Constants
from lazy_animal_state import LazyAnimalState, Location
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

    @staticmethod
    def recombine_fn(parent1: LazyAnimalState, parent2: LazyAnimalState) -> LazyAnimalState:
        t_len1 = len(parent1.toys)
        f_len1 = len(parent1.food)
        if t_len1 == 0:
            t_len1 = 1
            keep_toys = False
        else:
            keep_toys = True

        if f_len1 == 0:
            f_len1 = 1
            keep_food = False
        else:
            keep_food = True

        t_range1 = randrange(0, t_len1)
        f_range1 = randrange(0, f_len1)

        t_len2 = len(parent1.toys)
        f_len2 = len(parent1.food)

        if t_len2 == 0:
            t_len2 = 1
            take_toys = False
        else:
            take_toys = True

        if f_len2 == 0:
            f_len2 = 1
            take_food = False
        else:
            take_food = True

        t_range2 = randrange(0, t_len2)
        f_range2 = randrange(0, f_len2)

        # Keep these:
        if keep_toys:
            parent1.toys = parent1.toys[:t_range1]

        if keep_food:
            parent1.food = parent1.food[:f_range1]

        # Take these:
        if take_toys:
            parent1.toys.append(parent2.toys[t_range2:])

        if take_food:
            parent1.food.append(parent2.food[f_range2:])

        parent1.current_animal_kcalories = \
            round((parent1.current_animal_kcalories + parent2.current_animal_kcalories) / 2)

        # Note that we do not want to add a new state to the tree here,
        # but to combine attributes from two different states.

        return parent1

    @staticmethod
    def mutate_fn(x: LazyAnimalState, gene_pool: list, pmut: float) -> LazyAnimalState:
        if uniform(0, 1) >= pmut:
            return x

        n = len(x.tree_key)
        g = len(gene_pool)
        c = randrange(0, n)
        r = randrange(0, g)

        new_gene = gene_pool[r]
        # The gene, if unique, can be used to identify a new state.
        intermediate = x.tree_key[:c] + str(new_gene) + x.tree_key[c + 1:]

        # Note: Location does not have constraints --
        # If this changes, then these random values passed to it will need to be constrained accordingly.

        # Location, Calories burned by playing with toy, Boolean flag for IsPlayedWith.
        new_toy: Tuple[Location, int, bool] = (Location(c, r), len(intermediate)*10, False)
        new_food: Tuple[Location, int, bool] = (Location(c+1, r-1), len(intermediate)*10, False)
        # TODO: Ensure that toys and food are accounted for, by way of agent actions.
        # Same thing applies for human_location, and animal_location.
        # i.e. Locations on the way to the current state should be factored into the current state's value.
        x.toys.append(new_toy)
        x.food.append(new_food)
        x.current_animal_kcalories = len(intermediate)  # Start small, so we don't reach the goal right away.
        x.human_location = Location(c+2, r-2)
        x.animal_location = Location(c+3, r-3)

        return x
