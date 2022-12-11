import sys

from lazy_animal_state import LazyAnimalState

sys.path.append('aima-python')

from games import alpha_beta_search  # type: ignore
from lazy_animal_minimax_game1 import LazyAnimalMinimaxGame1


class MainHelper:
    def __init__(self):
        pass

    def help(self):
        pass


def main():

    game = LazyAnimalMinimaxGame1()

    initial_state = LazyAnimalState()
    initial_state.tree_key = 'A'
    initial_state.is_max = True

    ab_search_result = alpha_beta_search(initial_state, game)
    print('ab_search_result: ', ab_search_result)
    # Best Action (key) is returned from 'alpha_beta_search', but not the terminal state that it leads to.
    # Also note that it's possible that a goal state is not reached - seeing this happen.
    # Ideal: Return the whole path, from initial state to terminal state (and if goal was reached).
    #
    # Goal is not being reached because current_animal_kcalories is not being updated.


if __name__ == '__main__':
    main()
